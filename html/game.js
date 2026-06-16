document.addEventListener('DOMContentLoaded', async () => {
    // Top bar elements
    const pageTitle = document.getElementById('pageTitle');
    const pageDesc = document.getElementById('pageDesc');
    const tagsContainer = document.getElementById('tagsContainer');
    const btnFullscreen = document.getElementById('btnFullscreen');
    
    // Player elements
    const gameFrame = document.getElementById('gameFrame');
    const playerContainer = document.getElementById('playerContainer');
    
    // Info section elements
    const infoTitle = document.getElementById('infoTitle');
    const infoDesc = document.getElementById('infoDesc');
    const infoDev = document.getElementById('infoDev');
    const infoControls = document.getElementById('infoControls');
    const infoDate = document.getElementById('infoDate');
    const gameTagsContainer = document.getElementById('gameTagsContainer');
    const livePlayersCount = document.getElementById('livePlayersCount');

    // Get Game ID from URL
    const urlParams = new URLSearchParams(window.location.search);
    const gameId = urlParams.get('id');

    if (!gameId) {
        showError();
        return;
    }

    try {
        // Fetch games list from API
        const response = await fetch('/api/games?v=' + new Date().getTime());
        const data = await response.json();
        
        // Find matching game
        const game = data.games.find(g => g.slug === gameId);

        if (!game) {
            showError();
            return;
        }

        // Populate Top Bar
        pageTitle.textContent = game.title;
        pageDesc.textContent = game.short_description || game.description || 'Play instantly!';
        
        // Add to Recent History (Backend + Local)
        const token = localStorage.getItem('token');
        if (token) {
            fetch('/api/user/history', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${token}`
                },
                body: JSON.stringify({ slug: gameId, title: game.title })
            }).catch(e => console.error('Failed to log history', e));
        }
        // Save local history for guest users too
        let localHistory = JSON.parse(localStorage.getItem('playgamioHistory') || '[]');
        localHistory = localHistory.filter(s => s !== gameId);
        localHistory.unshift(gameId);
        if (localHistory.length > 20) localHistory = localHistory.slice(0, 20);
        localStorage.setItem('playgamioHistory', JSON.stringify(localHistory));
        
        // Populate Tags in Top Bar
        tagsContainer.innerHTML = '';
        if (gameTagsContainer) gameTagsContainer.innerHTML = '';
        
        if (game.categories && game.categories.length > 0) {
            game.categories.forEach(cat => {
                // Top bar tag
                const span = document.createElement('span');
                span.className = 'tag-pill';
                span.textContent = '#' + cat.toLowerCase();
                tagsContainer.appendChild(span);
                
                // Sidebar tag
                if (gameTagsContainer) {
                    const sideSpan = document.createElement('span');
                    sideSpan.className = 'bg-white/10 border border-white/10 text-gray-300 px-3 py-1 rounded-full text-xs font-semibold';
                    sideSpan.textContent = cat;
                    gameTagsContainer.appendChild(sideSpan);
                }
            });
        }
        
        // Populate Info Section
        infoTitle.textContent = game.title;
        infoDesc.textContent = game.description || 'Welcome to the game! Build your strategy, defeat enemies, and rule the leaderboards.';
        infoDev.textContent = game.developer || 'PlayGamio Studios';
        if (infoControls) infoControls.textContent = game.controls || 'Keyboard / Touch';
        if (infoDate) infoDate.textContent = game.release_date || 'Updated 2024';
        
        // Random live players count
        if (livePlayersCount) {
            livePlayersCount.textContent = Math.floor(Math.random() * (400 - 50) + 50);
        }
        
        // Setup loading state and event BEFORE setting src
        const iframeLoader = document.getElementById('iframeLoader');
        let isLoaded = false;
        
        const showGame = () => {
            if(isLoaded) return;
            isLoaded = true;
            gameFrame.classList.remove('opacity-0');
            gameFrame.classList.add('opacity-100');
            if(iframeLoader) {
                setTimeout(() => {
                    iframeLoader.style.display = 'none';
                }, 700);
            }
        };

        gameFrame.onload = showGame;
        
        // Fallback: If onload doesn't fire for some reason within 3 seconds, force show
        setTimeout(showGame, 3000);

        // Load the game immediately!
        gameFrame.src = game.url;

        // Setup Fullscreen
        const goFullscreen = () => {
            if (playerContainer.requestFullscreen) {
                playerContainer.requestFullscreen();
            } else if (playerContainer.webkitRequestFullscreen) {
                playerContainer.webkitRequestFullscreen();
            } else if (playerContainer.msRequestFullscreen) {
                playerContainer.msRequestFullscreen();
            }
        };

        btnFullscreen.addEventListener('click', goFullscreen);

        // Setup Upvote
        const btnUpvote = document.getElementById('btnUpvote');
        const upvoteText = document.getElementById('upvoteText');
        const upvotedGames = JSON.parse(localStorage.getItem('upvoted_games') || '[]');
        
        if (upvotedGames.includes(gameId)) {
            btnUpvote.classList.add('opacity-50', 'cursor-not-allowed');
            upvoteText.textContent = 'Upvoted';
            btnUpvote.disabled = true;
        }

        btnUpvote.addEventListener('click', () => {
            if (!upvotedGames.includes(gameId)) {
                upvotedGames.push(gameId);
                localStorage.setItem('upvoted_games', JSON.stringify(upvotedGames));
                btnUpvote.classList.add('opacity-50', 'cursor-not-allowed');
                upvoteText.textContent = 'Upvoted';
                btnUpvote.disabled = true;
            }
        });

        // Setup Share
        const btnShare = document.getElementById('btnShare');
        const shareText = document.getElementById('shareText');
        
        btnShare.addEventListener('click', async () => {
            try {
                if (navigator.share) {
                    await navigator.share({
                        title: `Play ${game.title} on PlayGamio!`,
                        text: game.description,
                        url: window.location.href,
                    });
                } else {
                    await navigator.clipboard.writeText(window.location.href);
                    shareText.textContent = 'Copied!';
                    setTimeout(() => shareText.textContent = 'Share', 2000);
                }
            } catch (err) {
                console.error('Error sharing:', err);
            }
        });

    } catch (error) {
        console.error('Error fetching game:', error);
        showError();
    }

    function showError() {
        pageTitle.textContent = "Game Not Found";
        pageDesc.textContent = "Error loading";
        infoTitle.textContent = "Game Not Found";
        infoDesc.textContent = "Sorry, we couldn't load this game. Please return to the homepage.";
    }
});
