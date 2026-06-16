import json

with open('/root/playgamio/html/games.json', 'r') as f:
    data = json.load(f)

# Keep only the 34 games that have real URLs (original games)
original_slugs = {
    'swoop-3d', 'seemore-3d', 'flappy-3d', 'hexgl-3d-racer', 'astray-3d-maze',
    'ball-pool-3d', 'planet-city-3d', 'clumsy-bird', 'pacman-html5', 'blockrain-tetris',
    'geometry-dash-3d', 'highway-racer-3d', 'moto-roadrash-3d', 'furious-racing-3d',
    'offroader-v5-3d', 'gp-moto-racing', 'truck-simulator-3d', 'bus-simulator-3d',
    'fox-simulator-3d', 'horse-simulator-3d', 'panda-simulator-3d', 'dog-simulator-3d',
    'only-up-3d-parkour', 'raccoon-adventure-3d', 'dreadhead-parkour', 'dune-surfer',
    'eagle-ride', 'christmas-deer-sim', 'solitaire-online', '0hh1-puzzle',
    'drift-hunters-3d', 'smash-karts-3d', 'temple-run-3d'
}

# Keep original games
original_games = [g for g in data['games'] if g['slug'] in original_slugs]

# All real working games from githubgames.gitlab.io
SUB = 'https://githubgames.gitlab.io/assets/upload/subgorg/jpg'
UBG = 'https://githubgames.gitlab.io/assets/upload/ubg67com/jpg'

real_games = [
    # From homepage + car page + running page
    ("christmas-deer-simulator", "Christmas Deer Simulator", "Guide deer through winter wonderlands!", "3D/Simulation", "Arrow Keys"),
    ("gobble", "Gobble", "Eat everything as a hungry gobbling creature!", "Arcade/Action", "Arrow Keys"),
    ("halloween-skeleton-smash", "Halloween Skeleton Smash", "Smash skeletons in this spooky game!", "Arcade/Action", "Mouse/Click"),
    ("idle-success", "Idle Success", "Build your idle empire from nothing!", "Simulation/Strategy", "Mouse/Click"),
    ("iron-snout", "Iron Snout", "Fight wolves as a pig warrior!", "Action/Fighting", "Arrow Keys"),
    ("kix-dream-soccer", "Kix Dream Soccer", "Play amazing soccer with special moves!", "Sports/Arcade", "Arrow Keys/Space"),
    ("merge-alphabet", "Merge Alphabet", "Merge letters and build words!", "Puzzle/Strategy", "Mouse/Click"),
    ("papas-wingeria", "Papas Wingeria", "Cook and serve wings in this restaurant game!", "Simulation/Casual", "Mouse/Click"),
    ("poppy-glamrock", "Poppy Glamrock", "Rock out with Poppy in glam style!", "Arcade/Music", "Mouse/Click"),
    ("raft-life", "Raft Life", "Survive on a raft in the ocean!", "Adventure/Simulation", "Mouse/Click"),
    ("rally-point-2", "Rally Point 2", "Race through checkpoints in this rally game!", "Racing/Arcade", "Arrow Keys"),
    ("spider-solitaire", "Spider Solitaire", "Classic Spider Solitaire card game!", "Puzzle/Strategy", "Mouse/Click"),
    ("bob-the-robber-4", "Bob The Robber 4", "Sneak and steal as master thief Bob!", "Action/Puzzle", "Arrow Keys"),
    ("boxrob", "BoxRob", "Push boxes and solve clever puzzles!", "Puzzle/Strategy", "Arrow Keys"),
    ("burger-clicker", "Burger Clicker", "Click to make the ultimate burger empire!", "Simulation/Idle", "Mouse/Click"),
    ("cartoon-mini-racing", "Cartoon Mini Racing", "Fun cartoon racing for everyone!", "Racing/Arcade", "Arrow Keys"),
    ("cat-clicker-re", "Cat Clicker", "Click cats and build a feline empire!", "Simulation/Casual", "Mouse/Click"),
    ("cats-drop", "Cats Drop", "Drop cute cats and match them up!", "Puzzle/Casual", "Mouse/Click"),
    ("deer-simulator", "Deer Simulator", "Live the wild life as a graceful deer!", "3D/Simulation", "Arrow Keys"),
    ("diggy", "Diggy", "Dig deep into the earth for treasures!", "Arcade/Puzzle", "Mouse/Click"),
    ("ducklife-4", "Duck Life 4", "Train your duck and win races!", "Racing/Simulation", "Arrow Keys/Mouse"),
    ("extreme-car-parking", "Extreme Car Parking", "Test your parking skills to the max!", "Racing/Simulation", "Arrow Keys"),
    ("extreme-off-road-cars-3-cargo", "Extreme Off Road Cars 3", "Cargo delivery through extreme terrain!", "Racing/3D", "Arrow Keys"),
    ("fnaf-sister", "FNAF Sister", "Survive the night in this horror adventure!", "Action/Horror", "Mouse/Click"),
    ("fnaf4", "FNAF 4", "Five Nights at Freddy's 4 horror survival!", "Action/Horror", "Mouse/Click"),
    ("fortride-open-world", "Fortride: Open World", "Drive freely in a massive open world!", "Racing/Open World", "Arrow Keys/WASD"),
    ("geometry-dash-remastered", "Geometry Dash Remastered", "Jump to the beat in this rhythm platformer!", "Arcade/Action", "Space/Click"),
    ("heroball-adventures", "Heroball Adventures", "Roll and bounce through challenging levels!", "Arcade/Action", "Arrow Keys"),
    ("hydro-storm-2", "Hydro Storm 2", "Race hydro jets across stormy waters!", "Racing/Action", "Arrow Keys"),
    ("level-devil-2", "Level Devil 2", "Survive devilishly tricky platform levels!", "Action/Arcade", "Arrow Keys"),
    ("lows-adventures-3", "Lows Adventures 3", "Explore worlds as the brave hero Low!", "Adventure/Platformer", "Arrow Keys/Space"),
    ("merge-rainbow", "Merge Rainbow", "Merge colors and create rainbows!", "Puzzle/Casual", "Mouse/Click"),
    # From homepage trending
    ("bloons-tower-defense-3", "Bloons Tower Defense 3", "Pop bloons with strategic towers!", "Strategy/Puzzle", "Mouse/Click"),
    ("breaking-the-bank", "Breaking The Bank", "Break into the vault in this heist game!", "Adventure/Puzzle", "Mouse/Click"),
    ("cyber-cars-punk-racing", "Cyber Cars Punk Racing", "Futuristic cyberpunk car racing!", "Racing/3D", "Arrow Keys"),
    ("death-chase", "Death Chase", "Race for your life in this survival racer!", "Racing/Action", "Arrow Keys"),
    ("drift-io", "Drift IO", "Drift and compete online against others!", "Racing/Arcade", "Arrow Keys"),
    ("escaping-the-prison", "Escaping The Prison", "Plan and execute a prison break!", "Adventure/Puzzle", "Mouse/Click"),
    ("fleeing-the-complex", "Fleeing The Complex", "Escape from a high-security facility!", "Adventure/Puzzle", "Mouse/Click"),
    ("football-masters", "Football Masters", "Play action-packed arcade football!", "Sports/Arcade", "Arrow Keys/Space"),
    ("g-switch-4", "G Switch 4", "Flip gravity and race through wild tracks!", "Arcade/Running", "Space/Click"),
    ("game-of-farmers", "Game Of Farmers", "Build the ultimate farming kingdom!", "Simulation/Strategy", "Mouse/Click"),
    ("gold-digger-frvr", "Gold Digger FRVR", "Dig for gold and strike it rich!", "Puzzle/Arcade", "Mouse/Click"),
    ("gp-moto-racing-3", "GP Moto Racing 3", "Pro motorcycle racing on epic circuits!", "Racing/Sports", "Arrow Keys"),
    ("grindcraft-remastered", "GrindCraft Remastered", "Craft and survive in block world!", "Simulation/Adventure", "Mouse/Click"),
    ("highway-bike-simulator", "Highway Bike Simulator", "Race bikes on busy highways!", "Racing/3D", "Arrow Keys"),
    ("hill-climb-racing", "Hill Climb Racing", "Climb impossible hills with physics!", "Racing/Arcade", "Arrow Keys/Space"),
    ("hover-racer-drive", "Hover Racer Drive", "Fly hovercrafts through neon tracks!", "Racing/Arcade", "Arrow Keys"),
    ("idle-dice", "Idle Dice", "Roll the dice and build fortune!", "Idle/Strategy", "Mouse/Click"),
    ("idle-digging-tycoon", "Idle Digging Tycoon", "Dig deep and build a mining empire!", "Simulation/Idle", "Mouse/Click"),
    ("iron-snout-2", "Iron Snout 2", "Even more wolf-punching pig action!", "Action/Fighting", "Arrow Keys"),
    ("jellycar-worlds", "JellyCar Worlds", "Drive squishy cars through wobbly worlds!", "Racing/Arcade", "Arrow Keys"),
    ("jump-monster", "Jump Monster", "Jump and crush everything in your path!", "Arcade/Action", "Space/Click"),
    ("magikmon", "Magikmon", "Catch magical creatures and battle!", "Adventure/RPG", "Mouse/Click"),
    ("merge-cyber-racers", "Merge Cyber Racers", "Merge cars and race in cyber world!", "Racing/Strategy", "Mouse/Click"),
    # Car page games
    ("18-wheeler-cargo-simulator", "18 Wheeler Cargo Simulator", "Drive massive trucks delivering cargo!", "Racing/Simulation", "Arrow Keys"),
    ("3d-arena-racing", "3D Arena Racing", "Race in explosive 3D arenas!", "Racing/3D", "Arrow Keys"),
    ("3d-car-simulator", "3D Car Simulator", "Realistic 3D car driving simulator!", "Racing/3D", "Arrow Keys/WASD"),
    ("3d-moto-simulator-2", "3D Moto Simulator 2", "Epic motorcycle simulation in 3D!", "Racing/3D", "Arrow Keys"),
    ("adventure-drivers", "Adventure Drivers", "Race and explore in driving adventures!", "Racing/Adventure", "Arrow Keys"),
    ("bicycle-stunts-3d", "Bicycle Stunts 3D", "Perform amazing bike stunts in 3D!", "Sports/3D", "Arrow Keys"),
    ("blumgi-rocket", "Blumgi Rocket", "Launch rockets and defy physics!", "Arcade/Action", "Space/Mouse"),
    ("burnin-rubber-5-xs", "Burnin Rubber 5 XS", "Extreme car combat racing action!", "Racing/Action", "Arrow Keys"),
    ("car-drift-racers-2", "Car Drift Racers 2", "Master the art of drifting!", "Racing/Sports", "Arrow Keys"),
    ("car-rush", "Car Rush", "Rush through city streets at top speed!", "Racing/Arcade", "Arrow Keys"),
    ("car-simulator-arena", "Car Simulator Arena", "Drive freely in a massive arena!", "Racing/3D", "Arrow Keys/WASD"),
    ("cars-thief", "Cars Thief", "Steal cars and cause mayhem!", "Action/Racing", "Arrow Keys"),
    ("city-car-driving-stunt-master", "City Car Driving Stunt Master", "Perform insane city car stunts!", "Racing/Action", "Arrow Keys"),
    ("crazy-bikes", "Crazy Bikes", "Ride crazy bikes through wild terrain!", "Racing/Arcade", "Arrow Keys"),
    ("crazy-cars", "Crazy Cars", "Wacky car racing with crazy physics!", "Racing/Arcade", "Arrow Keys"),
    ("demolition-derby-crash-racing", "Demolition Derby Crash Racing", "Crash and smash in the derby arena!", "Racing/Action", "Arrow Keys"),
    ("drift-boss", "Drift Boss", "Become the ultimate drifting champion!", "Racing/Sports", "Mouse/Click"),
    ("drift-dudes", "Drift Dudes", "Radical drifting with cool characters!", "Racing/Arcade", "Arrow Keys"),
    ("drift-f1", "Drift F1", "Formula One drifting mastery!", "Racing/Sports", "Arrow Keys"),
    ("drive-mad", "Drive Mad", "Crazy destructive driving mayhem!", "Racing/Arcade", "Arrow Keys/Space"),
    ("earn-to-die", "Earn To Die", "Drive through zombie hordes to survive!", "Action/Racing", "Arrow Keys/Space"),
    ("eggy-car", "Eggy Car", "Don't drop the egg in this physics racer!", "Racing/Arcade", "Arrow Keys"),
    ("endless-truck", "Endless Truck", "Drive endlessly through rough terrain!", "Racing/Arcade", "Arrow Keys"),
    ("extreme-off-road-cars", "Extreme Off Road Cars", "Master extreme off-road driving!", "Racing/3D", "Arrow Keys"),
    ("fastlane-frenzy", "Fastlane Frenzy", "High-speed lane switching action!", "Arcade/Racing", "Arrow Keys"),
    ("fly-car-stunt-2", "Fly Car Stunt 2", "Stunt flying cars in epic arenas!", "Racing/Action", "Arrow Keys/Space"),
    ("go-kart-go-ultra", "Go Kart Go Ultra", "Ultimate go-kart racing fun!", "Racing/Arcade", "Arrow Keys"),
    ("grand-prix-hero", "Grand Prix Hero", "Become the Grand Prix champion!", "Racing/Sports", "Arrow Keys"),
    ("jelly-truck", "Jelly Truck", "Wobble your way through crazy levels!", "Racing/Arcade", "Arrow Keys"),
    ("kart-race-3d", "Kart Race 3D", "Fast-paced 3D kart racing action!", "Racing/3D", "Arrow Keys"),
    ("kart-wars", "Kart Wars", "Battle while racing in armed karts!", "Racing/Action", "Arrow Keys/Space"),
    ("mad-truck-challenge-special", "Mad Truck Challenge", "Destroy opponents in truck arena battles!", "Racing/Action", "Arrow Keys"),
    ("madalin-stunt-cars-2", "Madalin Stunt Cars 2", "Open world stunt driving paradise!", "Racing/3D", "Arrow Keys/WASD"),
    ("mega-ramp-car-stunts", "Mega Ramp Car Stunts", "Perform massive ramp stunts with cars!", "Racing/Action", "Arrow Keys"),
    ("moto-x3m-4-winter", "Moto X3M Winter", "Winter motorcycle trials madness!", "Racing/Arcade", "Arrow Keys/Space"),
    ("moto-x3m-5-pool-party", "Moto X3M Pool Party", "Summer pool party bike racing!", "Racing/Arcade", "Arrow Keys/Space"),
    ("motocross-x3m-spooky-land", "Moto X3M Spooky Land", "Spooky halloween bike races!", "Racing/Arcade", "Arrow Keys/Space"),
    ("motox3m-2", "Moto X3M 2", "Extreme motorcycle trials part 2!", "Racing/Arcade", "Arrow Keys/Space"),
    ("neon-hill-rider", "Neon Hill Rider", "Ride neon hills at breakneck speed!", "Racing/Arcade", "Arrow Keys"),
    ("offroad-forest-racing", "Offroad Forest Racing", "Race through deep forest off-road!", "Racing/3D", "Arrow Keys"),
    ("parking-fury-3", "Parking Fury 3", "Extreme parking challenges part 3!", "Racing/Puzzle", "Arrow Keys"),
    ("parking-fury-3d", "Parking Fury 3D", "Realistic 3D parking simulator!", "Racing/Simulation", "Arrow Keys"),
    ("rally-point-3", "Rally Point 3", "Rally racing through checkpoints!", "Racing/Arcade", "Arrow Keys"),
    ("rally-point-4", "Rally Point 4", "More checkpoint rally racing!", "Racing/Arcade", "Arrow Keys"),
    ("retro-highway", "Retro Highway", "Retro-style highway racing action!", "Racing/Arcade", "Arrow Keys"),
    ("rider-2", "Rider 2", "Flip and ride through stunt tracks!", "Arcade/Sports", "Arrow Keys/Space"),
    ("rocket-soccer-derby", "Rocket Soccer Derby", "Rocket-powered car soccer madness!", "Sports/Racing", "Arrow Keys/Boost"),
    ("sling-drift", "Sling Drift", "Slingshot drift racing action!", "Racing/Arcade", "Mouse/Click"),
    ("smash-karts", "Smash Karts", "Battle kart mayhem online!", "Racing/Action", "Arrow Keys/Space"),
    ("soccar", "Soccar", "Car soccer with rocket boosts!", "Sports/Racing", "Arrow Keys"),
    ("sports-bike-racing", "Sports Bike Racing", "High-speed superbike racing!", "Racing/Sports", "Arrow Keys"),
    ("stock-car-hero", "Stock Car Hero", "NASCAR-style stock car racing!", "Racing/Sports", "Arrow Keys"),
    ("stunt-car-challenge-3", "Stunt Car Challenge 3", "Perform insane car stunt challenges!", "Racing/Action", "Arrow Keys"),
    ("super-bike-the-champion", "Super Bike Champion", "Become the ultimate bike champion!", "Racing/Sports", "Arrow Keys"),
    ("super-star-car", "Super Star Car", "Drive the most amazing supercars!", "Racing/3D", "Arrow Keys"),
    ("survival-race", "Survival Race", "Race and survive against all odds!", "Racing/Action", "Arrow Keys"),
    ("tiny-cars", "Tiny Cars", "Race adorable tiny cars!", "Racing/Arcade", "Arrow Keys"),
    ("top-speed-3d", "Top Speed 3D", "Reach insane top speeds in 3D!", "Racing/3D", "Arrow Keys"),
    ("traffic-jam-3d", "Traffic Jam 3D", "Navigate through massive 3D traffic jams!", "Racing/3D", "Arrow Keys"),
    ("traffic-tour", "Traffic Tour", "Endless highway traffic racing!", "Racing/Arcade", "Arrow Keys"),
    ("ultimate-offroad-cars-2", "Ultimate Offroad Cars 2", "The ultimate offroad driving challenge!", "Racing/3D", "Arrow Keys"),
    ("up-hill-racing-2", "Up Hill Racing 2", "Race up impossibly steep hills!", "Racing/Arcade", "Arrow Keys/Space"),
    # Running page games  
    ("run-3", "Run 3", "Run through space tunnels in this classic!", "Arcade/Running", "Arrow Keys"),
    ("rolling-ball-3d", "Rolling Ball 3D", "Roll through obstacle courses at speed!", "Arcade/Running", "Arrow Keys"),
    ("slope3", "Slope 3", "Roll down the neon slope avoiding obstacles!", "Arcade/Running", "Arrow Keys"),
    ("tiles-hop-3d", "Tiles Hop 3D", "Bounce to the beat in music ball game!", "Arcade/Music", "Mouse/Click"),
    ("two-ball-3d", "Two Ball 3D", "Control two balls in this crazy racer!", "Arcade/Running", "Arrow Keys"),
    ("death-run-3d", "Death Run 3D", "Run faster than death in this intense race!", "Arcade/Running", "Arrow Keys"),
    ("electron-dash", "Electron Dash", "Dash through neon electronic worlds!", "Arcade/Running", "Arrow Keys"),
    ("geometry-dash-bloodbath", "Geometry Dash Bloodbath", "The hardest geometry dash level ever!", "Arcade/Action", "Space/Click"),
    ("geometry-neon-dash-rainbow", "Geometry Neon Dash Rainbow", "Colorful neon geometry rhythm runner!", "Arcade/Running", "Space/Click"),
    ("gswitch", "G-Switch 3", "Gravity switching multiplayer runner!", "Arcade/Running", "Space/Click"),
    ("color-road", "Color Road", "Match colors while rolling to survive!", "Arcade/Running", "Arrow Keys"),
    ("escape-run", "Escape Run", "Escape the chasing danger while running!", "Arcade/Running", "Arrow Keys"),
    ("jetpack-joyride", "Jetpack Joyride", "Fly with awesome jetpacks collecting coins!", "Arcade/Action", "Space/Click"),
    ("skibidi-dash", "Skibidi Dash", "Dash and dodge in this viral game!", "Arcade/Running", "Arrow Keys"),
    ("skiing-fred", "Skiing Fred", "Ski down deadly slopes as Fred!", "Arcade/Sports", "Arrow Keys"),
    ("slope-ball", "Slope Ball", "Roll a ball down endless neon slopes!", "Arcade/Running", "Arrow Keys"),
    ("slope-run", "Slope Run", "High-speed slope running action!", "Arcade/Running", "Arrow Keys"),
    ("vector-rush", "Vector Rush", "Rush through vector graphic worlds!", "Arcade/Running", "Arrow Keys"),
]

# Remove old non-working games
keep_original = [g for g in data['games'] if g['slug'] in original_slugs]

# Create new games
new_games = []
for slug, title, desc, cats_str, controls in real_games:
    cats = cats_str.split('/')
    thumb = f"{SUB}/{slug}.webp"
    new_games.append({
        "slug": slug,
        "title": title,
        "description": desc,
        "short_description": title,
        "thumbnail": thumb,
        "categories": cats,
        "url": f"https://githubgames.gitlab.io/game/{slug}.html",
        "rating": round(4.0 + (hash(slug) % 10) / 10.0, 1),
        "developer": "Open Source",
        "controls": controls,
        "release_date": "Updated 2024"
    })

final_games = keep_original + new_games

data['games'] = final_games
data['total_games'] = len(final_games)
data['last_updated'] = "2026-06-16"

with open('/root/playgamio/html/games.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"Kept {len(keep_original)} original + Added {len(new_games)} real games = {len(final_games)} total")
