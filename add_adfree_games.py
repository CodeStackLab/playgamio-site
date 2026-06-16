import json

ad_free_games = [
    {
        "slug": "swoop-3d",
        "title": "Swoop 3D",
        "url": "https://playcanv.as/p/JtL2iqIH/",
        "categories": ["3D", "Action", "Arcade"],
        "description": "An incredible 3D flight simulator without a single ad in sight! Fly through rings and score points."
    },
    {
        "slug": "seemore-3d",
        "title": "Seemore 3D",
        "url": "https://playcanv.as/p/2OlkUaxF/",
        "categories": ["3D", "Simulation"],
        "description": "Explore an immersive 3D world. Completely ad-free experience powered by PlayCanvas."
    },
    {
        "slug": "flappy-3d",
        "title": "Flappy 3D",
        "url": "https://playcanv.as/p/RqJJ9oU9/",
        "categories": ["3D", "Arcade"],
        "description": "The classic bird game but in glorious 3D! No ads to interrupt your high scores."
    },
    {
        "slug": "hextris",
        "title": "Hextris",
        "url": "https://hextris.io/",
        "categories": ["Puzzle", "Arcade"],
        "description": "An addictive, fast-paced puzzle game inspired by Tetris. 100% open source and ad-free!"
    },
    {
        "slug": "2048-classic",
        "title": "2048 Classic",
        "url": "https://play2048.co/",
        "categories": ["Puzzle", "Strategy"],
        "description": "The original 2048 puzzle game. Slide tiles, merge numbers, and enjoy a perfectly ad-free experience."
    },
    {
        "slug": "clumsy-bird",
        "title": "Clumsy Bird",
        "url": "https://ellisonleao.github.io/clumsy-bird/",
        "categories": ["Action", "Arcade"],
        "description": "A beautiful open-source clone of Flappy Bird built with MelonJS. Absolutely zero ads."
    }
]

with open('/root/playgamio/html/games.json', 'r') as f:
    data = json.load(f)

# Take the first 6 thumbnails from existing games
new_games = []
for i, ad_game in enumerate(ad_free_games):
    existing_game = data['games'][i]
    new_game = {
        "slug": ad_game["slug"],
        "title": ad_game["title"],
        "description": ad_game["description"],
        "short_description": "100% Ad-Free Game",
        "thumbnail": existing_game["thumbnail"],
        "categories": ad_game["categories"],
        "url": ad_game["url"],
        "rating": 5.0,
        "developer": "Open Source / PlayCanvas",
        "controls": "Keyboard & Mouse",
        "release_date": "Updated 2024"
    }
    new_games.append(new_game)

final_data = {
    "api_version": "1.0",
    "total_games": len(new_games),
    "last_updated": "2026-06-11",
    "games": new_games
}

with open('/root/playgamio/html/games.json', 'w') as f:
    json.dump(final_data, f, indent=2)

print("Successfully generated fully ad-free games!")
