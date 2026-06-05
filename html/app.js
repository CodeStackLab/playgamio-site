// GAMES DATA
const AVAILABLE_GAMES = [
  {
    id: "hextris",
    name: "Hextris",
    genre: "Arcade",
    thumbnail: "https://images.unsplash.com/photo-1614850523459-c2f4c699c52e?auto=format&fit=crop&w=600&q=80",
    url: "https://hextris.github.io/hextris/",
    desc: "Fast-paced puzzle game inspired by Tetris. Rotate the hexagon to match colors!",
    hot: true,
    new: true
  },
  {
    id: "2048",
    name: "2048",
    genre: "Puzzle",
    thumbnail: "https://images.unsplash.com/photo-1611195974226-a6a9be9dd763?auto=format&fit=crop&w=600&q=80",
    url: "https://gabrielecirulli.github.io/2048/",
    desc: "Join the numbers and get to the 2048 tile! Highly addictive sliding puzzle game.",
    hot: true,
    new: false
  },
  {
    id: "clumsy-bird",
    name: "Clumsy Bird",
    genre: "Arcade",
    thumbnail: "https://images.unsplash.com/photo-1551103782-8ab07afd45c1?auto=format&fit=crop&w=600&q=80",
    url: "https://ellisonleao.github.io/clumsy-bird/",
    desc: "Flap your wings, avoid the green pipes, and try to get the highest score!",
    hot: false,
    new: true
  },
  {
    id: "pacman",
    name: "Pacman HTML5",
    genre: "Arcade",
    thumbnail: "https://images.unsplash.com/photo-1538481199705-c710c4e965fc?auto=format&fit=crop&w=600&q=80",
    url: "https://pacman-html5.github.io/",
    desc: "The classic Pacman retro experience. Eat all dots and avoid the ghosts!",
    hot: true,
    new: false
  },
  {
    id: "tower-game",
    name: "Tower Blocks",
    genre: "Strategy",
    thumbnail: "https://images.unsplash.com/photo-1607604276583-eef5d076aa5f?auto=format&fit=crop&w=600&q=80",
    url: "https://clement-muth.github.io/TowerGame/",
    desc: "Stack blocks as high as you can. Timed accuracy is the key to victory!",
    hot: false,
    new: true
  },
  {
    id: "offline-paradise",
    name: "Dino T-Rex",
    genre: "Action",
    thumbnail: "https://images.unsplash.com/photo-1506703719100-a0f3a48c0f86?auto=format&fit=crop&w=600&q=80",
    url: "https://chromedino.com/",
    desc: "The legendary Chrome offline dinosaur game. Jump over obstacles and survive.",
    hot: false,
    new: false
  }
];

const PLANNED_GAMES = [
  {
    id: "biz-empire",
    name: "BizEmpire",
    genre: "Business",
    thumbnail: "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?auto=format&fit=crop&w=600&q=80",
    votes: 42,
    hot: true
  },
  {
    id: "soccer-empire",
    name: "Soccer Empire",
    genre: "Sports",
    thumbnail: "https://images.unsplash.com/photo-1508098682722-e99c43a406b2?auto=format&fit=crop&w=600&q=80",
    votes: 28,
    hot: false
  },
  {
    id: "city-builder",
    name: "City Builder Tycoon",
    genre: "Tycoon",
    thumbnail: "https://images.unsplash.com/photo-1519501025264-65ba15a82390?auto=format&fit=crop&w=600&q=80",
    votes: 35,
    hot: true
  },
  {
    id: "tennis-boss",
    name: "Tennis Boss",
    genre: "Sports",
    thumbnail: "https://images.unsplash.com/photo-1595435934249-5df7ed86e1c0?auto=format&fit=crop&w=600&q=80",
    votes: 19,
    hot: false
  }
];

// DOM ELEMENTS
const genreBar = document.getElementById("genre-bar");
const gamesGrid = document.getElementById("gamesGrid");
const comingSoonGrid = document.getElementById("comingSoonGrid");
const featuredStrip = document.getElementById("featuredStrip");
const gameCountEl = document.getElementById("gameCount");
const searchInput = document.getElementById("searchInput");
const comingSoonSection = document.getElementById("comingSoonSection");

// VIEW SWITCHER DOM ELEMENTS
const viewGridBtn = document.getElementById("viewGrid");
const viewMapBtn = document.getElementById("viewMap");
const gridView = document.getElementById("gridView");
const mapView = document.getElementById("mapView");
const gameMapContainer = document.getElementById("gameMapContainer");
const mapZoomIn = document.getElementById("mapZoomIn");
const mapZoomOut = document.getElementById("mapZoomOut");
const mapCenter = document.getElementById("mapCenter");
const mapFullscreen = document.getElementById("mapFullscreen");
const selectedNodeGenre = document.getElementById("selectedNodeGenre");
const selectedNodeName = document.getElementById("selectedNodeName");
const selectedNodeDesc = document.getElementById("selectedNodeDesc");
const selectedNodeAction = document.getElementById("selectedNodeAction");
const availableCount = document.getElementById("availableCount");
const plannedCount = document.getElementById("plannedCount");

// MODAL DOM ELEMENTS
const gameModal = document.getElementById("gameModal");
const closeModal = document.getElementById("closeModal");
const fullscreenBtn = document.getElementById("fullscreenBtn");
const gameFrame = document.getElementById("gameFrame");
const gameFrameWrapper = document.getElementById("gameFrameWrapper");
const gameLoading = document.getElementById("gameLoading");
const modalGenre = document.getElementById("modalGenre");
const modalTitle = document.getElementById("modalTitle");
const modalDesc = document.getElementById("modalDesc");

// SIGNIN DOM ELEMENTS
const signinBtn = document.getElementById("signinBtn");
const signinModal = document.getElementById("signinModal");
const closeSignin = document.getElementById("closeSignin");

// STATE
let activeGenre = "all";
let searchQuery = "";
let votedGames = JSON.parse(localStorage.getItem("playgamio_voted") || "[]");
let activeView = "map"; // "grid" or "map"
let mapNetworkInstance = null;
let selectedMapGame = AVAILABLE_GAMES[0];

// INITIALIZE APP
function init() {
  renderGenres();
  renderGames();
  renderComingSoon();
  setupEventListeners();
  availableCount.textContent = AVAILABLE_GAMES.length;
  plannedCount.textContent = PLANNED_GAMES.length;
  updateSelectedNode(selectedMapGame, false);
  initGameMap();
}

// RENDER GENRES
function renderGenres() {
  genreBar.addEventListener("click", (e) => {
    const btn = e.target.closest(".genre-btn");
    if (!btn) return;

    document.querySelectorAll(".genre-btn").forEach(b => {
      b.classList.remove("active");
      b.setAttribute("aria-selected", "false");
    });
    btn.classList.add("active");
    btn.setAttribute("aria-selected", "true");

    activeGenre = btn.dataset.genre;
    
    if (activeView === "grid") {
      renderGames();
    } else {
      initGameMap(); // Redraw map to highlight or filter
    }
  });
}

// RENDER GAMES GRID & FEATURED
function renderGames() {
  gamesGrid.innerHTML = "";
  featuredStrip.innerHTML = "";

  const filtered = AVAILABLE_GAMES.filter(game => {
    const matchesGenre = activeGenre === "all" || game.genre.toLowerCase() === activeGenre.toLowerCase();
    const matchesSearch = game.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
                          (game.desc || "").toLowerCase().includes(searchQuery.toLowerCase());
    return matchesGenre && matchesSearch;
  });

  gameCountEl.textContent = `${filtered.length} game${filtered.length === 1 ? "" : "s"}`;

  // Populate Games
  filtered.forEach(game => {
    const card = document.createElement("div");
    card.className = "game-card";
    card.setAttribute("title", game.name);
    card.setAttribute("data-genre", game.genre);
    card.innerHTML = `
      <div class="shimmer"></div>
      <img src="${game.thumbnail}" alt="${game.name}" loading="lazy" onload="this.previousElementSibling.remove()" />
      <div class="card-overlay"></div>
      <div class="card-name">${game.name}</div>
      <div class="card-badge-row">
        ${game.hot ? `<span class="badge hot">🔥 Hot!</span>` : ""}
        ${game.new ? `<span class="badge new">✨ New!</span>` : ""}
      </div>
      <div class="card-badge-right">
        <span class="badge" style="background:rgba(255,255,255,0.1);">${game.genre}</span>
      </div>
    `;
    card.addEventListener("click", () => openGame(game));
    gamesGrid.appendChild(card);
  });

  // Populate Featured
  const featured = AVAILABLE_GAMES.filter(game => game.hot).slice(0, 3);
  featured.forEach((game, idx) => {
    const featItem = document.createElement("div");
    featItem.className = "feat-item";
    if (idx === 0) featItem.style.gridColumn = "span 2";
    featItem.innerHTML = `
      <img src="${game.thumbnail}" alt="${game.name}" />
      <div class="feat-overlay"></div>
      <div class="feat-badge-row">
        <span class="badge hot">🔥 Featured</span>
        <span class="badge" style="background:rgba(0,0,0,0.4);">${game.genre}</span>
      </div>
      <button class="feat-cta">Play ${game.name} Now</button>
    `;
    featItem.addEventListener("click", () => openGame(game));
    featuredStrip.appendChild(featItem);
  });
}

// RENDER COMING SOON
function renderComingSoon() {
  comingSoonGrid.innerHTML = "";

  PLANNED_GAMES.forEach(game => {
    const isVoted = votedGames.includes(game.id);
    const voteCount = game.votes + (isVoted ? 1 : 0);
    const card = document.createElement("div");
    card.className = "game-card";
    card.setAttribute("data-genre", game.genre);
    card.innerHTML = `
      <div class="shimmer"></div>
      <img src="${game.thumbnail}" alt="${game.name}" loading="lazy" onload="this.previousElementSibling.remove()" />
      <div class="card-overlay"></div>
      <div class="card-name">${game.name}</div>
      <div class="card-badge-row">
        <span class="badge soon">Coming Soon</span>
      </div>
      <button class="want-btn ${isVoted ? 'voted' : ''}" data-id="${game.id}">
        <span>${isVoted ? 'Voted' : 'I want this!'}</span> 💙 <span class="vote-count">${voteCount}</span>
      </button>
    `;

    const wantBtn = card.querySelector(".want-btn");
    wantBtn.addEventListener("click", (e) => {
      e.stopPropagation();
      toggleVote(game.id, wantBtn);
    });

    comingSoonGrid.appendChild(card);
  });
}

// VOTE LOGIC
function toggleVote(gameId, buttonEl) {
  if (votedGames.includes(gameId)) {
    votedGames = votedGames.filter(id => id !== gameId);
    buttonEl.classList.remove("voted");
    buttonEl.querySelector("span").textContent = "I want this!";
  } else {
    votedGames.push(gameId);
    buttonEl.classList.add("voted");
    buttonEl.querySelector("span").textContent = "Voted";
  }
  localStorage.setItem("playgamio_voted", JSON.stringify(votedGames));
  renderComingSoon();
}

// RENDER GAME UNIVERSE MAP (Vis-Network)
function initGameMap() {
  if (mapNetworkInstance) {
    mapNetworkInstance.destroy();
    mapNetworkInstance = null;
  }

  // Categories Color Mapping
  const genreColors = {
    "arcade": "#67de88", // Green
    "action": "#67de88", // Green
    "strategy": "#d2bbff", // Purple
    "tycoon": "#d2bbff", // Purple
    "business": "#d2bbff", // Purple
    "puzzle": "#4cd6ff", // Blue
    "sports": "#4cd6ff" // Blue
  };

  const nodes = [];
  const edges = [];

  // Central Core Node
  nodes.push({
    id: "hub",
    label: "🎮\nPLAYGAMIO",
    title: "PlayGamio Central Universe Hub",
    shape: "circle",
    size: 38,
    color: {
      background: "#06091F",
      border: "#67de88",
      highlight: { background: "#06091F", border: "#FAFAF5" }
    },
    font: { face: "Sora", size: 13, color: "#FAFAF5", bold: true },
    borderWidth: 3,
    shadow: true
  });

  // Keep track of genres added to prevent duplicates
  const activeGenres = new Set();

  const allGames = [...AVAILABLE_GAMES, ...PLANNED_GAMES];

  // Filter games based on search queries
  const matchesSearch = (game) => {
    return game.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
           (game.desc || "").toLowerCase().includes(searchQuery.toLowerCase());
  };

  allGames.forEach(game => {
    if (!matchesSearch(game)) return;
    
    // Add genre node if not added yet
    const genreKey = game.genre.toLowerCase();
    const isGenreActive = activeGenre === "all" || genreKey === activeGenre.toLowerCase();

    if (!activeGenres.has(genreKey)) {
      activeGenres.add(genreKey);
      const color = genreColors[genreKey] || "#dee0ff";
      
      nodes.push({
        id: `genre_${genreKey}`,
        label: game.genre,
        title: `${game.genre} Games Category`,
        shape: "dot",
      size: 22,
        color: {
          background: "#0e1228",
          border: color,
          highlight: { background: color, border: "#FAFAF5" }
        },
        font: { face: "Sora", size: 12, color: "#FAFAF5" },
        borderWidth: 2,
        opacity: isGenreActive ? 1.0 : 0.25,
        shadow: true
      });

      edges.push({
        from: "hub",
        to: `genre_${genreKey}`,
        color: { color: "rgba(103, 222, 136, 0.24)", highlight: color },
        width: 2.2,
        smooth: { type: "continuous" }
      });
    }

    // Add game node
    const isGameActive = isGenreActive;
    const isPlanned = !!game.votes;
    const color = genreColors[genreKey] || "#dee0ff";

    nodes.push({
      id: game.id,
      label: game.name,
      title: game.desc || `Help vote for ${game.name}!`,
      shape: "circularImage",
      image: game.thumbnail,
      size: isPlanned ? 24 : 29,
      color: {
        border: isPlanned ? "#00D1FF" : color,
        background: "#171a30",
        highlight: { border: "#FAFAF5", background: "#1b1e35" }
      },
      font: { face: "DM Sans", size: 11, color: "#dee0ff", strokeWidth: 4, strokeColor: "#06091F" },
      borderWidth: isPlanned ? 2 : 3,
      opacity: isGameActive ? 1.0 : 0.2,
      shadow: true,
      // Custom data payload
      gameData: game,
      isPlanned: isPlanned
    });

    edges.push({
      from: `genre_${genreKey}`,
      to: game.id,
      color: { color: isPlanned ? "rgba(0, 209, 255, 0.22)" : "rgba(255, 255, 255, 0.13)", highlight: color },
      width: isPlanned ? 1.2 : 1.7,
      dashes: isPlanned, // Dashed lines for coming soon games
      smooth: { type: "continuous" }
    });
  });

  // Vis-Network Configuration Options
  const container = gameMapContainer;
  const data = { nodes: new vis.DataSet(nodes), edges: new vis.DataSet(edges) };
  const options = {
    physics: {
      stabilization: {
        enabled: true,
        iterations: 220
      },
      barnesHut: {
        gravitationalConstant: -2300,
        centralGravity: 0.24,
        springLength: 122,
        springConstant: 0.038,
        damping: 0.12
      }
    },
    nodes: {
      shadow: {
        enabled: true,
        color: "rgba(103, 222, 136, 0.18)",
        size: 18,
        x: 0,
        y: 0
      }
    },
    edges: {
      shadow: {
        enabled: true,
        color: "rgba(0, 209, 255, 0.1)",
        size: 10,
        x: 0,
        y: 0
      }
    },
    interaction: {
      hover: true,
      dragNodes: true,
      zoomView: true,
      tooltipDelay: 120
    }
  };

  // Create network
  mapNetworkInstance = new vis.Network(container, data, options);

  // Set click handlers
  mapNetworkInstance.on("click", (params) => {
    if (params.nodes.length > 0) {
      const nodeId = params.nodes[0];
      const clickedNode = nodes.find(n => n.id === nodeId);
      
      if (clickedNode && clickedNode.gameData) {
        updateSelectedNode(clickedNode.gameData, clickedNode.isPlanned);
      }
      
      // Deselect node so it resets
      setTimeout(() => {
        if (mapNetworkInstance) mapNetworkInstance.unselectAll();
      }, 500);
    }
  });
}

function updateSelectedNode(game, isPlanned) {
  selectedMapGame = game;
  selectedNodeGenre.textContent = game.genre.toUpperCase();
  selectedNodeName.textContent = game.name;
  selectedNodeDesc.textContent = game.desc || `${game.name} is queued for the PlayGamio roadmap with ${game.votes} votes.`;
  selectedNodeAction.textContent = isPlanned ? `Vote ${game.votes + (votedGames.includes(game.id) ? 1 : 0)}` : "Play Now";
  selectedNodeAction.dataset.planned = isPlanned ? "true" : "false";
}

function runSelectedNodeAction() {
  const isPlanned = selectedNodeAction.dataset.planned === "true";
  if (!selectedMapGame) return;

  if (isPlanned) {
    votedGames = votedGames.includes(selectedMapGame.id)
      ? votedGames.filter(id => id !== selectedMapGame.id)
      : [...votedGames, selectedMapGame.id];
    localStorage.setItem("playgamio_voted", JSON.stringify(votedGames));
    updateSelectedNode(selectedMapGame, true);
    renderComingSoon();
    initGameMap();
    return;
  }

  openGame(selectedMapGame);
}

// EVENT LISTENERS
function setupEventListeners() {
  // Search
  searchInput.addEventListener("input", (e) => {
    searchQuery = e.target.value;
    if (activeView === "grid") {
      renderGames();
    } else {
      initGameMap();
    }
  });

  // Layout View Switcher
  viewGridBtn.addEventListener("click", () => {
    if (activeView === "grid") return;
    activeView = "grid";
    viewGridBtn.classList.add("active");
    viewGridBtn.setAttribute("aria-checked", "true");
    viewMapBtn.classList.remove("active");
    viewMapBtn.setAttribute("aria-checked", "false");
    
    gridView.classList.remove("hidden");
    mapView.classList.add("hidden");
    renderGames(); // Refresh grid layout
  });

  selectedNodeAction.addEventListener("click", runSelectedNodeAction);
  mapZoomIn.addEventListener("click", () => {
    if (!mapNetworkInstance) return;
    mapNetworkInstance.moveTo({ scale: mapNetworkInstance.getScale() * 1.18 });
  });
  mapZoomOut.addEventListener("click", () => {
    if (!mapNetworkInstance) return;
    mapNetworkInstance.moveTo({ scale: mapNetworkInstance.getScale() * 0.84 });
  });
  mapCenter.addEventListener("click", () => {
    if (mapNetworkInstance) mapNetworkInstance.fit({ animation: true });
  });
  mapFullscreen.addEventListener("click", () => {
    const wrapper = document.querySelector(".map-container-wrapper");
    if (wrapper.requestFullscreen) wrapper.requestFullscreen();
  });

  viewMapBtn.addEventListener("click", () => {
    if (activeView === "map") return;
    activeView = "map";
    viewMapBtn.classList.add("active");
    viewMapBtn.setAttribute("aria-checked", "true");
    viewGridBtn.classList.remove("active");
    viewGridBtn.setAttribute("aria-checked", "false");
    
    mapView.classList.remove("hidden");
    gridView.classList.add("hidden");
    initGameMap(); // Initialize network diagram
  });

  // Modals close triggers
  closeModal.addEventListener("click", closeGameModal);
  gameModal.addEventListener("click", (e) => {
    if (e.target === gameModal) closeGameModal();
  });

  // Fullscreen trigger
  fullscreenBtn.addEventListener("click", () => {
    if (gameFrameWrapper.requestFullscreen) {
      gameFrameWrapper.requestFullscreen();
    } else if (gameFrameWrapper.webkitRequestFullscreen) { /* Safari */
      gameFrameWrapper.webkitRequestFullscreen();
    } else if (gameFrameWrapper.msRequestFullscreen) { /* IE11 */
      gameFrameWrapper.msRequestFullscreen();
    }
  });

  // Signin triggers
  signinBtn.addEventListener("click", () => signinModal.classList.add("open"));
  closeSignin.addEventListener("click", () => signinModal.classList.remove("open"));
  signinModal.addEventListener("click", (e) => {
    if (e.target === signinModal) signinModal.classList.remove("open");
  });
  document.querySelector(".signin-submit").addEventListener("click", () => {
    alert("Sign In is under development. Have fun playing instant games!");
    signinModal.classList.remove("open");
  });
}

// OPEN GAME MODAL
function openGame(game) {
  modalTitle.textContent = game.name;
  modalGenre.textContent = game.genre;
  modalDesc.textContent = game.desc;
  
  gameLoading.classList.remove("hidden");
  gameFrame.src = game.url;

  gameModal.classList.add("open");
  document.body.style.overflow = "hidden"; // Prevent background scroll

  gameFrame.onload = () => {
    gameLoading.classList.add("hidden");
  };
}

// CLOSE GAME MODAL
function closeGameModal() {
  gameModal.classList.remove("open");
  gameFrame.src = "";
  document.body.style.overflow = ""; // Re-enable background scroll
}

// RUN APP
document.addEventListener("DOMContentLoaded", init);
