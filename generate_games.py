import json

with open('/tmp/fastgames.json', 'r') as f:
    fast_data = json.load(f)

all_fast_games = fast_data.get('games', [])

new_games = []

original_games = [
    {
      "slug": "biz-empire",
      "title": "Biz Empire",
      "description": "Build the ultimate business empire from scratch.",
      "short_description": "Build the ultimate business empire from scratch.",
      "thumbnail": "https://cdn.playgams.com/thumbnails/636de537-7c8f-4771-aa05-329941fb40fd/dd5e5f32-9c40-44f2-9109-41313cdcf585.webp",
      "categories": ["Business", "Tycoon"],
      "url": "https://playcanv.as/p/2OlkUaxF/",
      "rating": 4.9,
      "developer": "Friendly Pixels"
    },
    {
      "slug": "combat-gym",
      "title": "Combat Gym",
      "thumbnail": "https://cdn.playgams.com/thumbnails/34cbc0b8-204b-49b3-a733-64947e10ccd8/fd3da2a8-34b4-40a5-9073-ae6eef05a220.webp",
      "categories": ["Sports", "Action", "3D"],
      "url": "https://playcanv.as/p/2OlkUaxF/"
    },
    {
      "slug": "block-blast",
      "title": "Block Blast",
      "thumbnail": "https://cdn.playgams.com/thumbnails/a77c5f4a-2858-497e-8b13-7c0335c07f83/5ece72d3-7531-4e6a-9020-c8ccf636c312.webp",
      "categories": ["Puzzle", "Arcade"],
      "url": "https://playcanv.as/p/2OlkUaxF/"
    },
    {
      "slug": "boxing-dynasty",
      "title": "Boxing Dynasty",
      "thumbnail": "https://cdn.playgams.com/thumbnails/b98a2504-85c5-4740-9518-c803a8bd3f1a/1c2fe22d-5cd7-4882-8673-c7f61846df52.webp",
      "categories": ["Sports", "Action", "3D"],
      "url": "https://playcanv.as/p/2OlkUaxF/"
    },
    {
      "slug": "racing-fever",
      "title": "Racing Fever",
      "thumbnail": "https://cdn.playgams.com/thumbnails/41281364-c6bf-4ce9-9725-7f7080d5ac4a/a6d28362-9655-476e-96c2-ce7e6eaf2912.webp",
      "categories": ["Racing", "3D"],
      "url": "https://playcanv.as/p/2OlkUaxF/"
    },
    {
      "slug": "color-match",
      "title": "Color Match",
      "thumbnail": "https://cdn.playgams.com/thumbnails/5f9ff3e0-1084-41bc-a5c7-b2c659bdcd65/c8db78bb-769e-4245-9152-0c6fcc68cdf1.webp",
      "categories": ["Puzzle", "Casual"],
      "url": "https://playcanv.as/p/2OlkUaxF/"
    },
    {
      "slug": "cyber-wars",
      "title": "Cyber Wars",
      "thumbnail": "https://cdn.playgams.com/thumbnails/da17a30e-41a9-4ca7-90fc-7fb3c16fa618/2b128dc5-5d67-4a6a-93d1-425c64544d41.webp",
      "categories": ["Strategy", "Action", "3D"],
      "url": "https://playcanv.as/p/2OlkUaxF/"
    },
    {
      "slug": "market-trader",
      "title": "Market Trader",
      "thumbnail": "https://cdn.playgams.com/thumbnails/db6fd074-ffaf-4cd8-863c-a238990df13e/282fe848-baf2-4917-88ae-7a66e515b87a.webp",
      "categories": ["Business", "Strategy"],
      "url": "https://playcanv.as/p/2OlkUaxF/"
    }
]

for g in original_games:
    new_games.append({
        "slug": g["slug"],
        "title": g["title"],
        "description": g.get("description", "A great game!"),
        "short_description": g.get("short_description", "Play instantly!"),
        "thumbnail": g["thumbnail"],
        "categories": g["categories"],
        "url": g["url"],
        "rating": g.get("rating", 4.8),
        "developer": g.get("developer", "Friendly Pixels")
    })

allowed_cats = ["Business", "Strategy", "Arcade", "Sports", "Lifestyle", "Puzzle", "Tycoon", "Simulation", "Idle", "Action", "Racing", "3D"]

for game in all_fast_games:
    cats = game.get("categories", [])
    mapped_cats = []
    
    # Capitalize and filter
    for c in cats:
        cap = c.capitalize()
        if cap in allowed_cats:
            mapped_cats.append(cap)
            
    if not mapped_cats:
        mapped_cats = ["Arcade"] # fallback
        
    # Check for 3D in title
    if '3d' in game.get('title', '').lower():
        if "3D" not in mapped_cats:
            mapped_cats.append("3D")

    new_games.append({
        "slug": game.get("slug"),
        "title": game.get("title"),
        "description": game.get("description", game.get("short_description", "Play instantly!")),
        "short_description": game.get("short_description", "Awesome browser game"),
        "thumbnail": game.get("thumbnail"),
        "categories": mapped_cats,
        "url": game.get("url", "https://playcanv.as/p/2OlkUaxF/"),
        "rating": game.get("rating", 4.5),
        "developer": game.get("developer", "PlayGamio Studios")
    })

final_data = {
    "api_version": "1.0",
    "total_games": len(new_games),
    "last_updated": "2026-06-10",
    "games": new_games
}

with open('/root/playgamio/html/games.json', 'w') as f:
    json.dump(final_data, f, indent=2)

print(f"Successfully generated {len(new_games)} games!")
