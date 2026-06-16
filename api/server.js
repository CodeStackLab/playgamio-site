const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
const cors = require('cors');
const fs = require('fs');
const path = require('path');
const multer = require('multer');

const app = express();
app.use(express.json());
app.use(cors());

const JWT_SECRET = 'playgamio-super-secret-key-2026';
const DB_DIR = path.join(__dirname, 'db');
const GAMES_FILE = path.join(__dirname, 'games.json');
const UPLOADS_DIR = path.join(__dirname, 'uploads');

if (!fs.existsSync(UPLOADS_DIR)) {
    fs.mkdirSync(UPLOADS_DIR, { recursive: true });
}

const storage = multer.diskStorage({
    destination: (req, file, cb) => cb(null, UPLOADS_DIR),
    filename: (req, file, cb) => {
        const ext = path.extname(file.originalname).toLowerCase();
        const name = 'thumb_' + Date.now() + '_' + Math.random().toString(36).slice(2, 8) + ext;
        cb(null, name);
    }
});
const upload = multer({ 
    storage, 
    limits: { fileSize: 5 * 1024 * 1024 },
    fileFilter: (req, file, cb) => {
        const allowed = ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg'];
        const ext = path.extname(file.originalname).toLowerCase();
        cb(null, allowed.includes(ext));
    }
});

if (!fs.existsSync(DB_DIR)) {
    fs.mkdirSync(DB_DIR);
}

const db = new sqlite3.Database(path.join(DB_DIR, 'database.sqlite'));

function loadGames() {
    try {
        if (fs.existsSync(GAMES_FILE)) {
            const raw = fs.readFileSync(GAMES_FILE, 'utf-8');
            return JSON.parse(raw);
        }
    } catch (e) {
        console.error('Failed to load games.json:', e.message);
    }
    return { api_version: '1.0', total_games: 0, last_updated: '', games: [] };
}

function saveGames(data) {
    data.total_games = data.games.length;
    data.last_updated = new Date().toISOString().split('T')[0];
    fs.writeFileSync(GAMES_FILE, JSON.stringify(data, null, 2));
}

// Init DB
db.serialize(() => {
    db.run(`CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE,
        username TEXT,
        password TEXT,
        role TEXT DEFAULT 'user',
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )`);

    db.run(`CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        game_slug TEXT,
        game_title TEXT,
        played_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )`);
});

// Seed admin user from env vars
const ADMIN_EMAIL = process.env.ADMIN_EMAIL || 'admin@playgamio.com';
const ADMIN_PASSWORD = process.env.ADMIN_PASSWORD || 'Admin@2026!';

db.get('SELECT id FROM users WHERE email = ?', [ADMIN_EMAIL], (err, row) => {
    if (!row) {
        const hash = bcrypt.hashSync(ADMIN_PASSWORD, 10);
        db.run('INSERT INTO users (email, username, password, role) VALUES (?, ?, ?, ?)',
            [ADMIN_EMAIL, 'Admin', hash, 'admin'],
            function(e) {
                if (!e) console.log('Admin user seeded:', ADMIN_EMAIL);
            });
    }
});

// Middleware to verify JWT
const authenticateToken = (req, res, next) => {
    const authHeader = req.headers['authorization'];
    const token = authHeader && authHeader.split(' ')[1];
    if (!token) return res.sendStatus(401);
    jwt.verify(token, JWT_SECRET, (err, user) => {
        if (err) return res.sendStatus(403);
        req.user = user;
        next();
    });
};

// Admin middleware
const requireAdmin = (req, res, next) => {
    if (req.user.role !== 'admin') {
        return res.status(403).json({ error: 'Admin access required' });
    }
    next();
};

// ==================== AUTH ENDPOINTS ====================

app.post('/api/auth/register', (req, res) => {
    const { email, username, password } = req.body;
    if (!email || !password || !username) {
        return res.status(400).json({ error: 'All fields are required' });
    }
    const hashedPassword = bcrypt.hashSync(password, 10);
    db.run(`INSERT INTO users (email, username, password) VALUES (?, ?, ?)`, [email, username, hashedPassword], function(err) {
        if (err) return res.status(400).json({ error: 'Email already exists' });
        res.json({ message: 'User registered successfully!' });
    });
});

app.post('/api/auth/login', (req, res) => {
    const { email, password } = req.body;
    db.get(`SELECT * FROM users WHERE email = ?`, [email], (err, user) => {
        if (err || !user) return res.status(400).json({ error: 'Invalid email or password' });
        const validPassword = bcrypt.compareSync(password, user.password);
        if (!validPassword) return res.status(400).json({ error: 'Invalid email or password' });
        const token = jwt.sign({ id: user.id, username: user.username, email: user.email, role: user.role }, JWT_SECRET, { expiresIn: '7d' });
        res.json({ token, user: { username: user.username, email: user.email, role: user.role } });
    });
});

// ==================== USER ENDPOINTS ====================

app.get('/api/user/me', authenticateToken, (req, res) => {
    res.json(req.user);
});

app.get('/api/user/history', authenticateToken, (req, res) => {
    db.all(`SELECT game_slug, game_title, played_at FROM history WHERE user_id = ? ORDER BY played_at DESC LIMIT 20`, [req.user.id], (err, rows) => {
        if (err) return res.status(500).json({ error: err.message });
        res.json(rows);
    });
});

app.post('/api/user/history', authenticateToken, (req, res) => {
    const { slug, title } = req.body;
    if (!slug) return res.status(400).json({ error: 'Slug required' });
    db.run(`DELETE FROM history WHERE user_id = ? AND game_slug = ?`, [req.user.id, slug], () => {
        db.run(`INSERT INTO history (user_id, game_slug, game_title) VALUES (?, ?, ?)`, [req.user.id, slug, title || slug], function(err) {
            if (err) return res.status(500).json({ error: err.message });
            res.json({ success: true });
        });
    });
});

// ==================== PUBLIC GAMES ENDPOINT ====================

app.get('/api/games', (req, res) => {
    res.json(loadGames());
});

// ==================== ADMIN ENDPOINTS ====================

// Admin login (same as regular login but checks role)
app.post('/api/admin/login', (req, res) => {
    const { email, password } = req.body;
    db.get(`SELECT * FROM users WHERE email = ? AND role = 'admin'`, [email], (err, user) => {
        if (err || !user) return res.status(400).json({ error: 'Invalid admin credentials' });
        const validPassword = bcrypt.compareSync(password, user.password);
        if (!validPassword) return res.status(400).json({ error: 'Invalid admin credentials' });
        const token = jwt.sign({ id: user.id, username: user.username, email: user.email, role: user.role }, JWT_SECRET, { expiresIn: '7d' });
        res.json({ token, user: { username: user.username, email: user.email, role: user.role } });
    });
});

// List all games (admin - with extra info)
app.get('/api/admin/games', authenticateToken, requireAdmin, (req, res) => {
    const data = loadGames();
    res.json(data);
});

// Add a new game
app.post('/api/admin/games', authenticateToken, requireAdmin, (req, res) => {
    const { slug, title, description, short_description, thumbnail, categories, url, rating, developer, controls, release_date } = req.body;
    if (!slug || !title || !url) {
        return res.status(400).json({ error: 'slug, title, and url are required' });
    }
    const data = loadGames();
    if (data.games.find(g => g.slug === slug)) {
        return res.status(400).json({ error: 'A game with this slug already exists' });
    }
    const newGame = {
        slug,
        title,
        description: description || `Play ${title} instantly!`,
        short_description: short_description || title,
        thumbnail: thumbnail || 'https://via.placeholder.com/512',
        categories: categories || ['Arcade'],
        url,
        rating: rating || 4.5,
        developer: developer || 'PlayGamio Studios',
        controls: controls || 'Keyboard & Mouse',
        release_date: release_date || 'Updated ' + new Date().getFullYear()
    };
    data.games.push(newGame);
    saveGames(data);
    res.json({ message: 'Game added!', game: newGame });
});

// Update a game
app.put('/api/admin/games/:slug', authenticateToken, requireAdmin, (req, res) => {
    const data = loadGames();
    const idx = data.games.findIndex(g => g.slug === req.params.slug);
    if (idx === -1) return res.status(404).json({ error: 'Game not found' });
    data.games[idx] = { ...data.games[idx], ...req.body, slug: data.games[idx].slug };
    saveGames(data);
    res.json({ message: 'Game updated!', game: data.games[idx] });
});

// Delete a game
app.delete('/api/admin/games/:slug', authenticateToken, requireAdmin, (req, res) => {
    const data = loadGames();
    const idx = data.games.findIndex(g => g.slug === req.params.slug);
    if (idx === -1) return res.status(404).json({ error: 'Game not found' });
    const removed = data.games.splice(idx, 1)[0];
    saveGames(data);
    res.json({ message: 'Game deleted!', game: removed });
});

// Upload thumbnail
app.post('/api/admin/upload', authenticateToken, requireAdmin, upload.single('thumbnail'), (req, res) => {
    if (!req.file) return res.status(400).json({ error: 'No file uploaded' });
    const url = '/uploads/' + req.file.filename;
    res.json({ url, filename: req.file.filename });
});

// ==================== THIRD-PARTY GAME FETCHERS ====================

// Fetch from GamePix API
app.post('/api/admin/fetch-gamepix', authenticateToken, requireAdmin, (req, res) => {
    const { limit = 50 } = req.body;
    const https = require('https');
    const url = 'https://games.gamepix.com/games?sid=400';

    const reqOpts = {
        headers: { 'User-Agent': 'Mozilla/5.0' },
        rejectUnauthorized: false
    };

    https.get(url, reqOpts, (apiRes) => {
        let body = '';
        apiRes.on('data', chunk => body += chunk);
        apiRes.on('end', () => {
            try {
                const parsed = JSON.parse(body);
                if (parsed.status !== 'success') return res.status(500).json({ error: 'GamePix API returned non-success' });
                const games = parsed.data.slice(0, limit).map(g => ({
                    slug: (g.id || 'gamepix-' + Math.random().toString(36).slice(2, 8)).toLowerCase(),
                    title: g.title || 'Untitled',
                    description: g.description || 'Play this HTML5 game in your browser!',
                    short_description: (g.description || '').slice(0, 100),
                    thumbnail: g.thumbnailUrl || '',
                    categories: [g.category || 'Casual'],
                    url: `https://play.gamepix.com/${g.id}/embed?sid=1`,
                    rating: round(4.0 + ((g.rkScore || 0) * 0.1), 1),
                    developer: g.author || 'GamePix',
                    controls: 'Keyboard & Mouse',
                    release_date: 'Updated ' + new Date().getFullYear(),
                    _source: 'gamepix'
                }));
                res.json({ count: games.length, games });
            } catch (e) {
                res.status(500).json({ error: 'Failed to parse GamePix response: ' + e.message });
            }
        });
    }).on('error', e => res.status(500).json({ error: 'GamePix fetch failed: ' + e.message }));
});

// Fetch from GameDistribution RSS
app.post('/api/admin/fetch-gamedistribution', authenticateToken, requireAdmin, (req, res) => {
    const { limit = 42 } = req.body;
    const https = require('https');
    const url = 'https://catalog.api.gamedistribution.com/api/v2.0/rss/All/?format=json&amount=' + limit;

    https.get(url, { headers: { 'User-Agent': 'Mozilla/5.0' }, rejectUnauthorized: false }, (apiRes) => {
        let body = '';
        apiRes.on('data', chunk => body += chunk);
        apiRes.on('end', () => {
            try {
                const list = JSON.parse(body);
                const games = list.map(g => ({
                    slug: (g.Md5 || 'gd-' + Math.random().toString(36).slice(2, 8)).toLowerCase(),
                    title: g.Title || 'Untitled',
                    description: g.Description || '',
                    short_description: (g.Description || '').slice(0, 80),
                    thumbnail: (g.Asset && g.Asset[0]) || '',
                    categories: g.Category || ['Action'],
                    url: g.Url || '',
                    rating: 4.5,
                    developer: 'GameDistribution',
                    controls: g.Instructions || 'Mouse / Keyboard',
                    release_date: 'Updated ' + new Date().getFullYear(),
                    _source: 'gamedistribution'
                }));
                res.json({ count: games.length, games });
            } catch (e) {
                res.status(500).json({ error: 'Failed to parse GameDistribution response: ' + e.message });
            }
        });
    }).on('error', e => res.status(500).json({ error: 'GameDistribution fetch failed: ' + e.message }));
});

// Check if PlayCanvas game URLs are still alive
app.post('/api/admin/fetch-playcanvas', authenticateToken, requireAdmin, (req, res) => {
    const { slugs } = req.body;
    if (!slugs || !Array.isArray(slugs) || slugs.length === 0) {
        return res.status(400).json({ error: 'Provide an array of PlayCanvas project slugs' });
    }
    const https = require('https');
    const results = [];
    let done = 0;

    slugs.forEach(slug => {
        https.get(`https://playcanv.as/p/${slug}/`, { headers: { 'User-Agent': 'Mozilla/5.0' }, rejectUnauthorized: false }, (apiRes) => {
            const valid = apiRes.statusCode === 200;
            results.push({
                slug,
                url: `https://playcanv.as/p/${slug}/`,
                alive: valid,
                status: apiRes.statusCode
            });
            done++;
            if (done === slugs.length) res.json({ results });
        }).on('error', () => {
            results.push({ slug, url: `https://playcanv.as/p/${slug}/`, alive: false, status: 0 });
            done++;
            if (done === slugs.length) res.json({ results });
        });
    });
});

// Bulk import games from fetched list
app.post('/api/admin/games/bulk', authenticateToken, requireAdmin, (req, res) => {
    const { games } = req.body;
    if (!games || !Array.isArray(games) || games.length === 0) {
        return res.status(400).json({ error: 'Provide a games array' });
    }
    const data = loadGames();
    let added = 0;
    let skipped = 0;
    games.forEach(g => {
        const slug = (g.slug || '').toLowerCase().replace(/[^a-z0-9-]/g, '-');
        if (!slug || !g.title || !g.url) { skipped++; return; }
        if (data.games.find(existing => existing.slug === slug)) { skipped++; return; }
        data.games.push({
            slug,
            title: g.title,
            description: g.description || `Play ${g.title} instantly!`,
            short_description: g.short_description || g.title,
            thumbnail: g.thumbnail || 'https://via.placeholder.com/512',
            categories: g.categories || ['Arcade'],
            url: g.url,
            rating: g.rating || 4.5,
            developer: g.developer || 'PlayGamio Studios',
            controls: g.controls || 'Keyboard & Mouse',
            release_date: g.release_date || ('Updated ' + new Date().getFullYear())
        });
        added++;
    });
    saveGames(data);
    res.json({ message: `Added ${added} games, skipped ${skipped}`, added, skipped, total: data.games.length });
});

// ==================== HELPER ====================

function round(val, decimals) {
    const f = Math.pow(10, decimals);
    return Math.round(val * f) / f;
}

// ==================== START ====================

app.listen(3000, () => {
    console.log('Backend API running on port 3000');
});
