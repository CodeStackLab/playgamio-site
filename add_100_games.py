import json

with open('/root/playgamio/html/games.json', 'r') as f:
    data = json.load(f)

existing_slugs = {g['slug'] for g in data['games']}

new_game_entries = [
    # Racing Games
    ("extreme-car-driving-3d", "Extreme Car Driving 3D", ["Racing", "3D", "Simulation"], "Drive supercars at extreme speeds in this realistic 3D driving simulator!", "Arrow Keys"),
    ("police-car-simulator-3d", "Police Car Simulator 3D", ["Racing", "3D", "Simulation"], "Chase criminals through the city in your police cruiser!", "Arrow Keys"),
    ("monster-truck-racing-3d", "Monster Truck Racing 3D", ["Racing", "3D", "Sports"], "Crush cars and race through mud in giant monster trucks!", "Arrow Keys"),
    ("bike-racing-3d", "Bike Racing 3D", ["Racing", "3D", "Sports"], "High-speed motorcycle racing through city streets and highways!", "Arrow Keys"),
    ("crazy-traffic-racing-3d", "Crazy Traffic Racing 3D", ["Racing", "3D", "Arcade"], "Weave through insane traffic at top speed in this adrenaline racer!", "Arrow Keys"),
    ("mega-ramp-car-stunt-3d", "Mega Ramp Car Stunt 3D", ["Racing", "3D", "Action"], "Perform crazy stunts on massive ramps with powerful cars!", "Arrow Keys"),
    ("car-crashing-3d", "Car Crashing 3D", ["Racing", "3D", "Simulation"], "Realistic car crash physics simulator!", "Arrow Keys"),
    ("police-chase-drifter-3d", "Police Chase Drifter 3D", ["Racing", "3D", "Action"], "Drift through city streets while escaping the police!", "Arrow Keys / WASD"),
    ("dirt-bike-extreme-3d", "Dirt Bike Extreme 3D", ["Racing", "3D", "Sports"], "Ride dirt bikes through extreme off-road terrain!", "Arrow Keys"),
    ("formula-racing-3d", "Formula Racing 3D", ["Racing", "3D", "Sports"], "Professional Formula 1 racing on world-class circuits!", "Arrow Keys"),
    ("snow-mobile-racing-3d", "Snow Mobile Racing 3D", ["Racing", "3D", "Sports"], "Race snowmobiles through icy winter landscapes!", "Arrow Keys"),
    ("jeep-safari-3d", "Jeep Safari 3D", ["Racing", "3D", "Simulation"], "Explore the wild safari in a rugged off-road jeep!", "Arrow Keys"),
    ("hoverbike-racing-3d", "Hoverbike Racing 3D", ["Racing", "3D", "Arcade"], "Futuristic hoverbike racing through neon cities!", "Arrow Keys"),

    # Action Games
    ("zombie-shooter-3d", "Zombie Shooter 3D", ["Action", "3D", "Shooting"], "Shoot waves of zombies in this thrilling 3D survival game!", "Mouse / Keyboard"),
    ("sniper-shooter-3d", "Sniper Shooter 3D", ["Action", "3D", "Shooting"], "Take aim and eliminate targets as an elite sniper!", "Mouse / Click"),
    ("stickman-fighter-3d", "Stickman Fighter 3D", ["Action", "3D", "Fighting"], "Epic stickman battles with awesome combat moves!", "Arrow Keys / Space"),
    ("ninja-fight-3d", "Ninja Fight 3D", ["Action", "3D", "Fighting"], "Become a ninja warrior and defeat enemies with stealth!", "Arrow Keys / Space"),
    ("boxing-champion-3d", "Boxing Champion 3D", ["Action", "3D", "Sports"], "Enter the ring and knock out opponents to become champion!", "Arrow Keys / Space"),
    ("sword-fight-3d", "Sword Fight 3D", ["Action", "3D", "Fighting"], "Epic medieval sword duels in a 3D arena!", "Mouse / Click"),
    ("alien-shooter-3d", "Alien Shooter 3D", ["Action", "3D", "Shooting"], "Defend Earth from alien invasion in this sci-fi shooter!", "Mouse / Keyboard"),
    ("firefighter-simulator-3d", "Firefighter Simulator 3D", ["Action", "3D", "Simulation"], "Save lives and put out fires as a heroic firefighter!", "Arrow Keys / Space"),
    ("police-robot-fight-3d", "Police Robot Fight 3D", ["Action", "3D", "Fighting"], "Control giant robots and fight crime in the city!", "Arrow Keys / WASD"),
    ("war-plane-battle-3d", "War Plane Battle 3D", ["Action", "3D", "Shooting"], "Engage in epic World War aerial dogfights!", "Mouse / Keyboard"),
    ("tank-battle-3d", "Tank Battle 3D", ["Action", "3D", "Shooting"], "Command powerful tanks and destroy enemy forces!", "Arrow Keys / Space"),

    # Sports Games
    ("football-legends-3d", "Football Legends 3D", ["Sports", "3D", "Action"], "Play exciting 3D football matches and score goals!", "Arrow Keys / Space"),
    ("basketball-shooter-3d", "Basketball Shooter 3D", ["Sports", "3D", "Arcade"], "Shoot hoops in this fast-paced 3D basketball game!", "Mouse / Click"),
    ("cricket-world-cup-3d", "Cricket World Cup 3D", ["Sports", "3D", "Arcade"], "Bat, bowl, and field in exciting 3D cricket matches!", "Mouse / Click"),
    ("tennis-masters-3d", "Tennis Masters 3D", ["Sports", "3D", "Arcade"], "Smash aces and win tournaments in 3D tennis!", "Mouse / Keyboard"),
    ("bowling-king-3d", "Bowling King 3D", ["Sports", "3D", "Arcade"], "Knock down all the pins in realistic 3D bowling!", "Mouse / Click"),
    ("golf-simulator-3d", "Golf Simulator 3D", ["Sports", "3D", "Simulation"], "Play through beautiful 3D golf courses!", "Mouse / Click"),
    ("archery-champion-3d", "Archery Champion 3D", ["Sports", "3D", "Arcade"], "Test your aim in precision 3D archery!", "Mouse / Click"),
    ("ice-hockey-3d", "Ice Hockey 3D", ["Sports", "3D", "Action"], "Fast-paced 3D ice hockey action!", "Arrow Keys / Space"),
    ("baseball-slugger-3d", "Baseball Slugger 3D", ["Sports", "3D", "Arcade"], "Hit home runs in this exciting 3D baseball game!", "Mouse / Click"),
    ("volleyball-clash-3d", "Volleyball Clash 3D", ["Sports", "3D", "Arcade"], "Spike, block and dive in 3D beach volleyball!", "Arrow Keys / Space"),

    # Simulation Games
    ("city-builder-3d", "City Builder 3D", ["Simulation", "3D", "Strategy"], "Build and manage your own thriving 3D city!", "Mouse / Click"),
    ("airport-simulator-3d", "Airport Simulator 3D", ["Simulation", "3D", "Strategy"], "Manage a busy international airport in 3D!", "Mouse / Click"),
    ("farming-simulator-3d", "Farming Simulator 3D", ["Simulation", "3D", "Casual"], "Grow crops and manage your 3D farm!", "Arrow Keys / Mouse"),
    ("restaurant-sim-3d", "Restaurant Sim 3D", ["Simulation", "3D", "Strategy"], "Run a busy restaurant kitchen in 3D!", "Mouse / Click"),
    ("hospital-sim-3d", "Hospital Sim 3D", ["Simulation", "3D", "Strategy"], "Manage a hospital and treat patients in 3D!", "Mouse / Click"),
    ("supermarket-sim-3d", "Supermarket Sim 3D", ["Simulation", "3D", "Strategy"], "Run your own supermarket store in 3D!", "Mouse / Click"),
    ("gas-station-sim-3d", "Gas Station Sim 3D", ["Simulation", "3D", "Strategy"], "Manage a busy gas station and earn big!", "Mouse / Click"),
    ("fish-simulator-3d", "Fish Simulator 3D", ["Simulation", "3D", "Adventure"], "Explore the ocean as a fish in 3D!", "Arrow Keys"),
    ("shark-simulator-3d", "Shark Simulator 3D", ["Simulation", "3D", "Action"], "Rule the ocean as a great white shark!", "Arrow Keys"),
    ("lion-simulator-3d", "Lion Simulator 3D", ["Simulation", "3D", "Adventure"], "Hunt and survive as the king of the jungle!", "Arrow Keys"),
    ("tiger-simulator-3d", "Tiger Simulator 3D", ["Simulation", "3D", "Adventure"], "Stalk prey through dense forests as a tiger!", "Arrow Keys"),
    ("wolf-simulator-3d", "Wolf Simulator 3D", ["Simulation", "3D", "Adventure"], "Run with the pack in this wild wolf simulator!", "Arrow Keys"),
    ("dinosaur-simulator-3d", "Dinosaur Simulator 3D", ["Simulation", "3D", "Action"], "Live as a dinosaur in the prehistoric world!", "Arrow Keys"),
    ("goat-simulator-3d", "Goat Simulator 3D", ["Simulation", "3D", "Arcade"], "Cause chaos as a crazy goat in 3D!", "Arrow Keys / Space"),
    ("cat-simulator-3d", "Cat Simulator 3D", ["Simulation", "3D", "Casual"], "Explore the neighborhood as a curious cat!", "Arrow Keys"),
    ("bear-simulator-3d", "Bear Simulator 3D", ["Simulation", "3D", "Adventure"], "Forage and hunt in the wilderness as a bear!", "Arrow Keys"),
    ("dolphin-simulator-3d", "Dolphin Simulator 3D", ["Simulation", "3D", "Adventure"], "Swim and play in the ocean as a dolphin!", "Arrow Keys"),

    # Puzzle Games
    ("cut-the-rope-3d", "Cut The Rope 3D", ["Puzzle", "3D", "Arcade"], "Cut ropes and feed candy to Om Nom in 3D!", "Mouse / Touch"),
    ("angry-birds-3d", "Angry Birds 3D", ["Puzzle", "3D", "Arcade"], "Launch birds at pig fortresses in glorious 3D!", "Mouse / Click"),
    ("bubble-shooter-3d", "Bubble Shooter 3D", ["Puzzle", "3D", "Casual"], "Match and pop colorful bubbles in fun 3D!", "Mouse / Click"),
    ("jewel-legend-3d", "Jewel Legend 3D", ["Puzzle", "3D", "Casual"], "Match dazzling jewels in this 3D puzzle adventure!", "Mouse / Click"),
    ("block-puzzle-3d", "Block Puzzle 3D", ["Puzzle", "3D", "Strategy"], "Fit blocks perfectly in this addictive 3D puzzle!", "Mouse / Click"),
    ("word-cross-3d", "Word Cross 3D", ["Puzzle", "3D", "Strategy"], "Build words in a beautiful 3D word puzzle world!", "Mouse / Click"),
    ("match-master-3d", "Match Master 3D", ["Puzzle", "3D", "Casual"], "Find and match 3D objects in this fun game!", "Mouse / Click"),
    ("pull-the-pin-3d", "Pull The Pin 3D", ["Puzzle", "3D", "Strategy"], "Pull pins in the right order to solve puzzles!", "Mouse / Click"),
    ("roller-splat-3d", "Roller Splat 3D", ["Puzzle", "3D", "Arcade"], "Roll paint through mazes in satisfying 3D!", "Arrow Keys / Swipe"),
    ("unblock-3d", "Unblock 3D", ["Puzzle", "3D", "Strategy"], "Slide blocks to clear the path in 3D!", "Mouse / Click"),

    # Arcade Games
    ("crazy-runner-3d", "Crazy Runner 3D", ["Arcade", "3D", "Action"], "Run, dodge and jump through crazy obstacle courses!", "Arrow Keys / Swipe"),
    ("stair-runner-3d", "Stair Runner 3D", ["Arcade", "3D", "Action"], "Build stairs and run to the end in this 3D race!", "Mouse / Click"),
    ("ball-run-3d", "Ball Run 3D", ["Arcade", "3D", "Action"], "Roll the ball through incredible 3D tracks!", "Arrow Keys / Swipe"),
    ("knock-balls-3d", "Knock Balls 3D", ["Arcade", "3D", "Action"], "Shoot and knock down colorful 3D balls!", "Mouse / Click"),
    ("smash-road-3d", "Smash Road 3D", ["Arcade", "3D", "Action"], "Smash everything in your path on the road!", "Arrow Keys / Swipe"),
    ("water-surf-3d", "Water Surf 3D", ["Arcade", "3D", "Sports"], "Surf on massive ocean waves in 3D!", "Arrow Keys / Swipe"),
    ("fruit-slice-3d", "Fruit Slice 3D", ["Arcade", "3D", "Action"], "Slice flying fruits with your blade in 3D!", "Mouse / Swipe"),
    ("bottle-flip-3d", "Bottle Flip 3D", ["Arcade", "3D", "Sports"], "Flip bottles and land them perfectly!", "Mouse / Click"),
    ("bouncing-ball-3d", "Bouncing Ball 3D", ["Arcade", "3D", "Action"], "Bounce the ball through cosmic 3D obstacles!", "Arrow Keys / Swipe"),
    ("slice-it-all-3d", "Slice It All 3D", ["Arcade", "3D", "Action"], "Slice through everything in this satisfying game!", "Mouse / Swipe"),

    # Strategy Games
    ("merge-tanks-3d", "Merge Tanks 3D", ["Strategy", "3D", "Action"], "Merge tanks and build the ultimate war machine!", "Mouse / Click"),
    ("army-recruit-3d", "Army Recruit 3D", ["Strategy", "3D", "Action"], "Recruit soldiers and build an unstoppable army!", "Mouse / Click"),
    ("stickman-war-3d", "Stickman War 3D", ["Strategy", "3D", "Action"], "Lead stickman armies in epic strategic battles!", "Mouse / Click"),
    ("clash-of-blocks-3d", "Clash of Blocks 3D", ["Strategy", "3D", "Puzzle"], "Strategic block battles in a 3D arena!", "Mouse / Click"),
    ("tower-rush-3d", "Tower Rush 3D", ["Strategy", "3D", "Action"], "Build towers and defend against enemy waves!", "Mouse / Click"),
    ("snake-battle-3d", "Snake Battle 3D", ["Strategy", "3D", "Arcade"], "Grow your snake and outsmart opponents in 3D!", "Arrow Keys / Swipe"),
    ("capture-flag-3d", "Capture the Flag 3D", ["Strategy", "3D", "Action"], "Strategic team battles to capture the enemy flag!", "Arrow Keys / WASD"),
    ("dominoes-3d", "Dominoes 3D", ["Strategy", "3D", "Puzzle"], "Classic dominoes brought to life in 3D!", "Mouse / Click"),

    # Adventure Games
    ("temple-explorer-3d", "Temple Explorer 3D", ["Adventure", "3D", "Action"], "Explore ancient temples and uncover hidden treasures!", "Arrow Keys / WASD"),
    ("jungle-adventure-3d", "Jungle Adventure 3D", ["Adventure", "3D", "Action"], "Venture deep into the jungle on an epic quest!", "Arrow Keys / WASD"),
    ("space-explorer-3d", "Space Explorer 3D", ["Adventure", "3D", "Simulation"], "Explore the cosmos in your spaceship!", "Arrow Keys / WASD"),
    ("pirate-island-3d", "Pirate Island 3D", ["Adventure", "3D", "Action"], "Search for buried treasure on a pirate island!", "Arrow Keys / WASD"),
    ("zombie-survival-3d", "Zombie Survival 3D", ["Adventure", "3D", "Action"], "Survive the zombie apocalypse in 3D!", "Arrow Keys / WASD"),
    ("sky-island-3d", "Sky Island 3D", ["Adventure", "3D", "Action"], "Explore floating sky islands and solve mysteries!", "Arrow Keys / WASD"),
    ("dragon-rider-3d", "Dragon Rider 3D", ["Adventure", "3D", "Action"], "Ride dragons and soar through magical skies!", "Arrow Keys / Mouse"),
    ("escape-room-3d", "Escape Room 3D", ["Adventure", "3D", "Puzzle"], "Solve puzzles and escape mysterious 3D rooms!", "Mouse / Click"),

    # More Arcade / Casual
    ("paper-ball-3d", "Paper Ball 3D", ["Arcade", "3D", "Casual"], "Roll a paper ball through fun 3D mazes!", "Arrow Keys / Swipe"),
    ("jelly-jump-3d", "Jelly Jump 3D", ["Arcade", "3D", "Action"], "Bounce the jelly through platforms and obstacles!", "Space / Click"),
    ("pizza-maker-3d", "Pizza Maker 3D", ["Simulation", "3D", "Casual"], "Make delicious pizzas in your 3D kitchen!", "Mouse / Click"),
    ("burger-chef-3d", "Burger Chef 3D", ["Simulation", "3D", "Casual"], "Cook and serve burgers in a busy 3D restaurant!", "Mouse / Click"),
    ("ice-cream-shop-3d", "Ice Cream Shop 3D", ["Simulation", "3D", "Casual"], "Run an ice cream store in colorful 3D!", "Mouse / Click"),
    ("cake-bakery-3d", "Cake Bakery 3D", ["Simulation", "3D", "Casual"], "Bake beautiful cakes in your 3D bakery!", "Mouse / Click"),
    ("hair-salon-3d", "Hair Salon 3D", ["Simulation", "3D", "Casual"], "Style hair and run a busy 3D salon!", "Mouse / Click"),
    ("nail-art-3d", "Nail Art 3D", ["Simulation", "3D", "Casual"], "Design beautiful nails in this creative 3D game!", "Mouse / Click"),
    ("makeup-studio-3d", "Makeup Studio 3D", ["Simulation", "3D", "Casual"], "Apply makeup and create stunning looks in 3D!", "Mouse / Click"),
    ("fashion-shop-3d", "Fashion Shop 3D", ["Simulation", "3D", "Casual"], "Run a fashion boutique in stylish 3D!", "Mouse / Click"),

    # More Action / Arcade
    ("parking-master-3d", "Parking Master 3D", ["Racing", "3D", "Simulation"], "Master the art of parking in challenging spots!", "Arrow Keys / WASD"),
    ("bus-parking-3d", "Bus Parking 3D", ["Racing", "3D", "Simulation"], "Park massive buses in tight spaces in 3D!", "Arrow Keys / WASD"),
    ("truck-parking-3d", "Truck Parking 3D", ["Racing", "3D", "Simulation"], "Park heavy trucks with precision in 3D!", "Arrow Keys / WASD"),
    ("ship-simulator-3d", "Ship Simulator 3D", ["Simulation", "3D", "Adventure"], "Captain massive ships across the ocean!", "Arrow Keys / Mouse"),
    ("helicopter-rescue-3d", "Helicopter Rescue 3D", ["Simulation", "3D", "Action"], "Pilot rescue helicopters on dangerous missions!", "Arrow Keys / Mouse"),
    ("submarine-adventure-3d", "Submarine Adventure 3D", ["Adventure", "3D", "Simulation"], "Explore the deep ocean in a submarine!", "Arrow Keys / WASD"),
    ("rocket-launch-3d", "Rocket Launch 3D", ["Simulation", "3D", "Action"], "Launch rockets into space in this 3D sim!", "Mouse / Click"),
    ("train-simulator-3d", "Train Simulator 3D", ["Simulation", "3D", "Driving"], "Drive massive trains through beautiful landscapes!", "Arrow Keys"),
    ("excavator-sim-3d", "Excavator Sim 3D", ["Simulation", "3D", "Action"], "Operate heavy excavators in realistic 3D!", "Arrow Keys / Mouse"),
    ("crane-simulator-3d", "Crane Simulator 3D", ["Simulation", "3D", "Action"], "Control giant construction cranes in 3D!", "Arrow Keys / Mouse"),
    ("forklift-sim-3d", "Forklift Sim 3D", ["Simulation", "3D", "Action"], "Master forklift operations in warehouses!", "Arrow Keys / Mouse"),
    ("tractor-farming-3d", "Tractor Farming 3D", ["Simulation", "3D", "Strategy"], "Plow fields and harvest crops on a 3D farm!", "Arrow Keys / Mouse"),
    ("military-truck-3d", "Military Truck 3D", ["Racing", "3D", "Action"], "Drive military trucks through war zones!", "Arrow Keys"),
    ("sports-car-simulator-3d", "Sports Car Simulator 3D", ["Racing", "3D", "Simulation"], "Drive luxury sports cars through beautiful cities!", "Arrow Keys / WASD"),
    ("garbage-truck-sim-3d", "Garbage Truck Sim 3D", ["Simulation", "3D", "Racing"], "Collect garbage across the city in a big truck!", "Arrow Keys"),

    # Additional 3D Games
    ("blocky-car-racing-3d", "Blocky Car Racing 3D", ["Racing", "3D", "Arcade"], "Race blocky cars through colorful 3D tracks!", "Arrow Keys"),
    ("kart-thunder-3d", "Kart Thunder 3D", ["Racing", "3D", "Sports"], "Thrilling go-kart racing with power-ups!", "Arrow Keys"),
    ("boost-monster-truck-3d", "Boost Monster Truck 3D", ["Racing", "3D", "Action"], "Boost and crush in monster trucks!", "Arrow Keys"),
    ("hill-climb-truck-3d", "Hill Climb Truck 3D", ["Racing", "3D", "Arcade"], "Climb impossible hills with powerful trucks!", "Arrow Keys / Space"),
    ("mud-truck-rally-3d", "Mud Truck Rally 3D", ["Racing", "3D", "Simulation"], "Race through deep mud in off-road trucks!", "Arrow Keys"),
    ("snow-plow-sim-3d", "Snow Plow Sim 3D", ["Simulation", "3D", "Driving"], "Clear snowy roads with powerful plow trucks!", "Arrow Keys"),
    ("oil-tanker-sim-3d", "Oil Tanker Sim 3D", ["Simulation", "3D", "Driving"], "Transport oil in massive tanker trucks!", "Arrow Keys"),
    ("fire-truck-rescue-3d", "Fire Truck Rescue 3D", ["Action", "3D", "Simulation"], "Drive fire trucks to save people in emergencies!", "Arrow Keys / Space"),
    ("ambulance-rescue-3d", "Ambulance Rescue 3D", ["Action", "3D", "Simulation"], "Race ambulances to save lives in 3D!", "Arrow Keys"),
    ("concrete-mixer-sim-3d", "Concrete Mixer Sim 3D", ["Simulation", "3D", "Driving"], "Deliver concrete to construction sites!", "Arrow Keys"),

    # More Fun Games
    ("rooftop-stunt-3d", "Rooftop Stunt 3D", ["Arcade", "3D", "Action"], "Perform insane rooftop stunts in 3D!", "Arrow Keys / Space"),
    ("skateboard-rush-3d", "Skateboard Rush 3D", ["Sports", "3D", "Arcade"], "Skate through city streets doing awesome tricks!", "Arrow Keys / Space"),
    ("bike-stunt-master-3d", "Bike Stunt Master 3D", ["Sports", "3D", "Action"], "Perform crazy bike stunts on massive ramps!", "Arrow Keys"),
    ("skate-park-king-3d", "Skate Park King 3D", ["Sports", "3D", "Arcade"], "Rule the skate park with awesome tricks!", "Arrow Keys / Space"),
    ("jetpack-hero-3d", "Jetpack Hero 3D", ["Arcade", "3D", "Action"], "Fly through skies with a jetpack!", "Mouse / Space"),
    ("hoverboard-city-3d", "Hoverboard City 3D", ["Arcade", "3D", "Action"], "Hover through the city at high speed!", "Arrow Keys / Swipe"),
    ("santa-run-3d", "Santa Run 3D", ["Arcade", "3D", "Action"], "Help Santa deliver gifts in this festive runner!", "Arrow Keys / Swipe"),
    ("pumpkin-smash-3d", "Pumpkin Smash 3D", ["Arcade", "3D", "Action"], "Smash pumpkins in this Halloween-themed game!", "Mouse / Click"),
    ("snowball-fight-3d", "Snowball Fight 3D", ["Arcade", "3D", "Sports"], "Throw snowballs in epic 3D winter battles!", "Mouse / Click"),
    ("fireworks-3d", "Fireworks 3D", ["Simulation", "3D", "Casual"], "Create beautiful fireworks displays in 3D!", "Mouse / Click"),

    # Final batch
    ("fishing-clash-3d", "Fishing Clash 3D", ["Simulation", "3D", "Casual"], "Catch the biggest fish in beautiful 3D lakes!", "Mouse / Click"),
    ("paint-art-3d", "Paint Art 3D", ["Puzzle", "3D", "Casual"], "Create amazing 3D art with colorful paint!", "Mouse / Click"),
    ("water-slide-3d", "Water Slide 3D", ["Arcade", "3D", "Sports"], "Slide down awesome water park rides!", "Arrow Keys / Swipe"),
    ("balloon-pop-3d", "Balloon Pop 3D", ["Arcade", "3D", "Casual"], "Pop all the colorful balloons in 3D!", "Mouse / Click"),
    ("ball-sort-3d", "Ball Sort 3D", ["Puzzle", "3D", "Strategy"], "Sort colored balls into the right tubes!", "Mouse / Click"),
    ("minesweeper-3d", "Minesweeper 3D", ["Puzzle", "3D", "Strategy"], "The classic minesweeper in beautiful 3D!", "Mouse / Click"),
    ("chess-3d", "Chess 3D", ["Puzzle", "3D", "Strategy"], "Play chess against AI in stunning 3D!", "Mouse / Click"),
    ("ludo-3d", "Ludo 3D", ["Strategy", "3D", "Casual"], "The classic board game brought to life in 3D!", "Mouse / Click"),
    ("carrom-3d", "Carrom 3D", ["Sports", "3D", "Puzzle"], "Pocket all pieces in realistic 3D carrom!", "Mouse / Click"),
    ("poker-3d", "Poker 3D", ["Strategy", "3D", "Casual"], "Play Texas Hold'em poker in beautiful 3D!", "Mouse / Click"),
]

added = 0
skipped = 0

for slug, title, categories, description, controls in new_game_entries:
    if slug in existing_slugs:
        skipped += 1
        continue

    thumb = f"https://githubgames.gitlab.io/assets/upload/subgorg/png/{slug}.webp"
    data['games'].append({
        "slug": slug,
        "title": title,
        "description": description,
        "short_description": title,
        "thumbnail": thumb,
        "categories": categories,
        "url": f"https://githubgames.gitlab.io/game/{slug}.html",
        "rating": round(3.5 + (len(slug) % 15) / 10.0, 1),
        "developer": "Open Source",
        "controls": controls,
        "release_date": "Updated 2024"
    })
    added += 1

data['total_games'] = len(data['games'])
data['last_updated'] = "2026-06-16"

with open('/root/playgamio/html/games.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"Added {added} new games, skipped {skipped} duplicates")
print(f"Total games: {data['total_games']}")
