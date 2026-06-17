document.addEventListener('DOMContentLoaded', () => {
    const heroSection = document.getElementById('heroSection');
    const heroGrid = document.getElementById('heroGrid');
    const mainSection = document.getElementById('mainSection');
    const mainGrid = document.getElementById('mainGrid');
    const plannedSection = document.getElementById('plannedSection');
    const plannedGrid = document.getElementById('plannedGrid');
    const categoryNav = document.getElementById('categoryNav');
    const scrollLeftBtn = document.getElementById('scrollLeftBtn');
    const scrollRightBtn = document.getElementById('scrollRightBtn');
    const loadingIndicator = document.getElementById('loadingIndicator');

    if (scrollLeftBtn && categoryNav) {
        scrollLeftBtn.addEventListener('click', () => {
            categoryNav.scrollBy({ left: -200, behavior: 'smooth' });
        });
    }
    if (scrollRightBtn && categoryNav) {
        scrollRightBtn.addEventListener('click', () => {
            categoryNav.scrollBy({ left: 200, behavior: 'smooth' });
        });
    }
    
    // Auth and History
    const historySection = document.getElementById('historySection');
    const historyGrid = document.getElementById('historyGrid');
    const navAuthBtn = document.getElementById('navAuthBtn');
    const navAuthText = document.getElementById('navAuthText');
    const navAuthIcon = document.getElementById('navAuthIcon');
    const loginModal = document.getElementById('loginModal');
    const closeModal = document.getElementById('closeModal');
    const usernameInput = document.getElementById('usernameInput');
    
    // Check login status on load for history
    const historyToken = localStorage.getItem('token');
    const historyUser = JSON.parse(localStorage.getItem('user') || 'null');
    let currentUser = historyUser;
    let userHistory = JSON.parse(localStorage.getItem('playgamioHistory') || '[]');
    
    let allGames = [];
    let currentCategory = 'All';

    // Mock data for Planned section
    const plannedGames = [
        { title: 'City Builder', img: 'https://images.unsplash.com/photo-1480714378408-67cf0d13bc1b?auto=format&fit=crop&w=400&q=80', votes: 8 },
        { title: 'Yacht Life', img: 'https://images.unsplash.com/photo-1567899378494-47b22a2ae96a?auto=format&fit=crop&w=400&q=80', votes: 12 },
        { title: 'Restaurant Star', img: 'https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?auto=format&fit=crop&w=400&q=80', votes: 5 },
        { title: 'Farm Frenzy', img: 'https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&w=400&q=80', votes: 9 },
        { title: 'Tower Defense X', img: 'https://images.unsplash.com/photo-1542751371-adc38448a05e?auto=format&fit=crop&w=400&q=80', votes: 3 },
        { title: 'Tennis Boss', img: 'https://images.unsplash.com/photo-1595435934249-5df7ed86e1c0?auto=format&fit=crop&w=400&q=80', votes: 15 }
    ];

    // Fetch games from API
    async function fetchGames() {
        try {
            const response = await fetch('/api/games?v=' + new Date().getTime());
            const data = await response.json();
            // Randomize array to show different games on the front page
            allGames = data.games.sort(() => Math.random() - 0.5);
            renderCategories();
            renderGames();
        } catch (error) {
            console.error('Error fetching games:', error);
            loadingIndicator.innerHTML = `<div class="text-red-400 font-bold">Failed to load games. Please try again.</div>`;
        }
    }

    // Render categories dynamically based on available games
    function renderCategories() {
        const catSet = new Set();
        allGames.forEach(g => {
            if (g.categories) {
                g.categories.forEach(c => catSet.add(c));
            }
        });
        const uniqueCats = Array.from(catSet).sort();
        
        categoryNav.innerHTML = `
            <button data-cat="All" class="category-btn active flex items-center gap-1.5">
                <span class="material-symbols-outlined" style="font-size: 16px;">grid_view</span> All
            </button>
        `;
        
        uniqueCats.forEach(cat => {
            const btn = document.createElement('button');
            btn.className = 'category-btn';
            btn.dataset.cat = cat;
            btn.textContent = cat;
            if (currentCategory === cat) {
                btn.classList.add('active');
                categoryNav.querySelector('[data-cat="All"]').classList.remove('active');
            }
            categoryNav.appendChild(btn);
        });
    }

    // Render games based on category
    function renderGames() {
        heroGrid.innerHTML = '';
        mainGrid.innerHTML = '';
        
        loadingIndicator.classList.add('hidden');
        heroSection.classList.remove('hidden');
        mainSection.classList.remove('hidden');
        plannedSection.classList.remove('hidden');

        let filteredGames = allGames;
        if (currentCategory !== 'All') {
            filteredGames = allGames.filter(g => g.categories && g.categories.some(c => c.toLowerCase() === currentCategory.toLowerCase()));
        }

        // Sort by rating for hero section, and then by slug to prevent random shuffling on refresh
        const sorted = [...filteredGames].sort((a,b) => (b.rating || 0) - (a.rating || 0) || a.slug.localeCompare(b.slug));
        
        // Take top 3 for Hero Section
        const heroGamesList = sorted.slice(0, 3);
        const mainGamesList = sorted.slice(3, 200); // show all available games

        // 1. Render Hero Section
        if (heroGamesList.length === 0) {
            heroSection.classList.add('hidden');
        } else {
            heroGamesList.forEach((game, idx) => {
                const card = document.createElement('div');
                // First card is big, others are small
                const spanClass = idx === 0 ? 'lg:col-span-2 lg:row-span-2 min-h-[300px]' : 'lg:col-span-1 lg:row-span-1 min-h-[200px] lg:min-h-0';
                card.className = `hero-card bg-black/40 group relative overflow-hidden rounded-2xl ${spanClass}`;
                
                let badge = idx === 0 ? `<div class="absolute top-4 left-4 flex gap-2 z-20">
                    <span class="badge badge-hot text-sm px-3 py-1">🔥 Hot!</span>
                    <span class="badge badge-new text-sm px-3 py-1">✨ New!</span>
                </div>` : `<div class="absolute top-3 left-3 z-20"><span class="badge badge-new">✨ New!</span></div>`;

                const titleClass = idx === 0 ? 'text-3xl lg:text-5xl' : 'text-xl lg:text-2xl';
                const buttonClass = idx === 0 ? 'px-8 py-3 text-lg' : 'px-5 py-2 text-sm';

                card.innerHTML = `
                    <img src="${game.image || game.thumbnail}" alt="${game.title}" class="absolute inset-0 w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 opacity-90">
                    ${badge}
                    <div class="absolute inset-0 bg-gradient-to-t from-black via-black/40 to-transparent z-10 pointer-events-none"></div>
                    <div class="absolute inset-0 z-20 flex flex-col justify-end p-5 lg:p-8">
                        <div class="transform translate-y-4 group-hover:translate-y-0 transition-transform duration-300">
                            <h3 class="font-display font-bold ${titleClass} text-white mb-3 text-shadow-lg drop-shadow-md">${game.title}</h3>
                            <button class="bg-indigo-600/90 hover:bg-indigo-500 text-white font-bold ${buttonClass} rounded-full transition-colors w-max backdrop-blur-sm shadow-lg border border-white/10">
                                Play Now!
                            </button>
                        </div>
                    </div>
                `;
                card.addEventListener('click', () => { window.location.href = 'game.html?v=9.9&id=' + game.slug; });
                heroGrid.appendChild(card);
            });
        }

        // 2. Render Main Grid
        if (mainGamesList.length === 0) {
            mainGrid.innerHTML = `<div class="col-span-full text-center text-gray-400 py-12">No games found for this category.</div>`;
        } else {
            mainGamesList.forEach((game, idx) => {
                const card = document.createElement('div');
                card.className = 'grid-card group flex flex-col';
                
                let badge = '';
                if (idx % 7 === 0) badge = `<span class="badge badge-hot absolute top-2 left-2 z-10">🔥 Hot!</span>`;
                else if (idx % 5 === 0) badge = `<span class="badge badge-new absolute top-2 left-2 z-10">✨ New!</span>`;

                card.innerHTML = `
                    <div class="relative w-full h-full overflow-hidden bg-black/50">
                        ${badge}
                        <img src="${game.image || game.thumbnail}" alt="${game.title}" class="w-full h-full object-cover opacity-80 group-hover:opacity-100 group-hover:scale-110 transition-all duration-500">
                        
                        <!-- Hover Play Button overlay -->
                        <div class="absolute inset-0 bg-black/40 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center backdrop-blur-sm">
                            <button class="bg-white/20 hover:bg-white/30 border border-white/30 rounded-full w-12 h-12 flex items-center justify-center text-white backdrop-blur-md transform scale-50 group-hover:scale-100 transition-all duration-300">
                                <span class="material-symbols-outlined text-[24px]">play_arrow</span>
                            </button>
                        </div>
                    </div>
                `;
                card.addEventListener('click', () => { window.location.href = 'game.html?v=9.9&id=' + game.slug; });
                mainGrid.appendChild(card);
            });
        }

        // 3. Render Planned Section (Mock Data)
        plannedGrid.innerHTML = '';
        plannedGames.forEach(game => {
            const card = document.createElement('div');
            card.className = 'planned-card group';
            card.innerHTML = `
                <img src="${game.img}" alt="${game.title}" class="w-full h-full object-cover opacity-60 group-hover:opacity-80 transition-opacity">
                <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-transparent to-black/30"></div>
                
                <span class="badge badge-hot absolute top-2 left-2">🔥 Hot!</span>
                
                <div class="absolute bottom-0 left-0 w-full p-3 flex flex-col items-center gap-2 transform translate-y-2 group-hover:translate-y-0 transition-transform">
                    <h4 class="font-display font-bold text-white text-sm text-center text-shadow">${game.title}</h4>
                    <button class="bg-white/10 hover:bg-white/20 border border-white/20 text-white text-[11px] font-semibold px-4 py-1.5 rounded-full w-full flex items-center justify-center gap-1 transition-colors backdrop-blur-md">
                        I want this! <span class="text-blue-400">💙 ${game.votes}</span>
                    </button>
                </div>
            `;
            plannedGrid.appendChild(card);
        });

        // 4. Render History Section
        if (currentUser && userHistory.length > 0) {
            historySection.classList.remove('hidden');
            historyGrid.innerHTML = '';
            
            // Map history slugs back to game objects, filter out missing ones
            const historyGames = userHistory.map(slug => allGames.find(g => g.slug === slug)).filter(Boolean);
            
            if (historyGames.length > 0) {
                historyGames.slice(0, 6).forEach((game) => {
                    const card = document.createElement('div');
                    card.className = 'grid-card group flex flex-col';
                    
                    card.innerHTML = `
                        <div class="relative w-full h-full overflow-hidden bg-black/50 border border-indigo-500/30">
                            <img src="${game.image || game.thumbnail}" alt="${game.title}" class="w-full h-full object-cover opacity-80 group-hover:opacity-100 group-hover:scale-110 transition-all duration-500">
                            <div class="absolute inset-0 bg-black/40 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center backdrop-blur-sm">
                                <button class="bg-white/20 hover:bg-white/30 border border-white/30 rounded-full w-12 h-12 flex items-center justify-center text-white backdrop-blur-md transform scale-50 group-hover:scale-100 transition-all duration-300">
                                    <span class="material-symbols-outlined text-[24px]">play_arrow</span>
                                </button>
                            </div>
                        </div>
                    `;
                    card.addEventListener('click', () => { window.location.href = 'game.html?v=9.9&id=' + game.slug; });
                    historyGrid.appendChild(card);
                });
            } else {
                historySection.classList.add('hidden');
            }
        } else {
            if (historySection) historySection.classList.add('hidden');
        }
    }

    // --- Backend Authentication ---
    const authForm = document.getElementById('authForm');
    const tabLogin = document.getElementById('tabLogin');
    const tabRegister = document.getElementById('tabRegister');
    const usernameField = document.getElementById('usernameField');
    const authUsernameInput = document.getElementById('authUsernameInput');
    const authEmailInput = document.getElementById('authEmailInput');
    const authPasswordInput = document.getElementById('authPasswordInput');
    const authSubmitBtn = document.getElementById('authSubmitBtn');
    const authModalTitle = document.getElementById('authModalTitle');
    const authErrorMsg = document.getElementById('authErrorMsg');
    
    let isRegisterMode = false;
    
    // Check login status on load
    const token = localStorage.getItem('token');
    const user = JSON.parse(localStorage.getItem('user') || 'null');
    
    function updateAuthUI() {
        if (token && user) {
            navAuthText.textContent = 'Dashboard';
            navAuthIcon.textContent = 'dashboard';
        } else {
            navAuthText.textContent = 'Sign In';
            navAuthIcon.textContent = 'account_circle';
        }
    }
    updateAuthUI();

    navAuthBtn.addEventListener('click', () => {
        if (token && user) {
            window.location.href = '/dashboard.html';
        } else {
            loginModal.classList.remove('hidden');
            setTimeout(() => {
                loginModal.classList.remove('opacity-0');
                loginModal.firstElementChild.classList.remove('scale-95');
            }, 10);
        }
    });

    closeModal.addEventListener('click', () => {
        loginModal.classList.add('opacity-0');
        loginModal.firstElementChild.classList.add('scale-95');
        setTimeout(() => loginModal.classList.add('hidden'), 300);
    });

    // Toggle Tabs
    tabLogin.addEventListener('click', () => {
        isRegisterMode = false;
        authModalTitle.textContent = 'Log in';
        authSubmitBtn.textContent = 'Log In';
        usernameField.classList.add('hidden');
        authUsernameInput.required = false;
        authErrorMsg.classList.add('hidden');
        
        tabLogin.classList.replace('text-gray-400', 'text-white');
        tabLogin.classList.replace('hover:text-white', 'bg-indigo-600');
        tabRegister.classList.replace('text-white', 'text-gray-400');
        tabRegister.classList.replace('bg-indigo-600', 'hover:text-white');
    });

    tabRegister.addEventListener('click', () => {
        isRegisterMode = true;
        authModalTitle.textContent = 'Create Account';
        authSubmitBtn.textContent = 'Sign Up';
        usernameField.classList.remove('hidden');
        authUsernameInput.required = true;
        authErrorMsg.classList.add('hidden');
        
        tabRegister.classList.replace('text-gray-400', 'text-white');
        tabRegister.classList.replace('hover:text-white', 'bg-indigo-600');
        tabLogin.classList.replace('text-white', 'text-gray-400');
        tabLogin.classList.replace('bg-indigo-600', 'hover:text-white');
    });

    // Handle Auth Submit
    if(authForm) {
        authForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            authErrorMsg.classList.add('hidden');
            authSubmitBtn.disabled = true;
            authSubmitBtn.textContent = 'Processing...';

            const payload = {
                email: authEmailInput.value,
                password: authPasswordInput.value
            };
            if (isRegisterMode) payload.username = authUsernameInput.value;

            try {
                // Simulate network delay
                await new Promise(resolve => setTimeout(resolve, 500));
                
                // Using LocalStorage to simulate a database for the static site
                let users = JSON.parse(localStorage.getItem('playgamio_users') || '[]');

                if (isRegisterMode) {
                    if (users.find(u => u.email === payload.email)) {
                        throw new Error('Email is already registered!');
                    }
                    const newUser = {
                        id: Date.now().toString(),
                        email: payload.email,
                        username: payload.username,
                        password: payload.password // In a real app, never store plain text passwords
                    };
                    users.push(newUser);
                    localStorage.setItem('playgamio_users', JSON.stringify(users));

                    // Automatically switch to login after successful registration
                    tabLogin.click();
                    authErrorMsg.textContent = 'Account created successfully! Please log in.';
                    authErrorMsg.classList.remove('hidden', 'text-red-400');
                    authErrorMsg.classList.add('text-emerald-400');
                } else {
                    // Login mode
                    const user = users.find(u => u.email === payload.email && u.password === payload.password);
                    if (!user) {
                        throw new Error('Invalid email or password!');
                    }

                    // Login successful
                    localStorage.setItem('token', 'demo-token-' + user.id);
                    localStorage.setItem('user', JSON.stringify({ id: user.id, email: user.email, username: user.username }));
                    window.location.reload();
                }
            } catch (err) {
                authErrorMsg.textContent = err.message;
                authErrorMsg.classList.remove('hidden', 'text-emerald-400');
                authErrorMsg.classList.add('text-red-400');
            } finally {
                authSubmitBtn.disabled = false;
                authSubmitBtn.textContent = isRegisterMode ? 'Sign Up' : 'Log In';
            }
        });
    }

    // --- Dynamic Rendering ---

    // Initialize UI
    updateAuthUI();

    // Category Filter logic
    categoryNav.addEventListener('click', (e) => {
        const btn = e.target.closest('.category-btn');
        if (!btn) return;
        
        document.querySelectorAll('.category-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        
        currentCategory = btn.dataset.cat;
        renderGames();
    });

    // Initial Fetch
    fetchGames();
});
