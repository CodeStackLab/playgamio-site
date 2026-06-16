import json
import re

content = open('/root/playgamio/playgams.html').read()

tiles = re.findall(r'<div class="fp-tile fp-game-tile" aria-label="([^"]+)".*?<img class="fp-tile-img" src="([^"]+)"', content)
tiles2 = re.findall(r'<a class="fp-tile fp-game-tile" aria-label="([^"]+)".*?<img class="fp-tile-img" src="([^"]+)"', content)

all_tiles = tiles + tiles2

categories = ["Business", "Strategy", "Arcade", "Sports", "Lifestyle", "Puzzle", "Tycoon", "Simulation", "Idle", "Action", "Racing", "3D"]

games = []
for i, (title, img) in enumerate(all_tiles):
    # assign a category
    cat = categories[i % len(categories)]
    
    # some basic matching
    title_lower = title.lower()
    if 'sport' in title_lower or 'tennis' in title_lower or 'soccer' in title_lower or 'nba' in title_lower or 'golf' in title_lower:
        cat = "Sports"
    elif 'empire' in title_lower or 'tycoon' in title_lower or 'boss' in title_lower or 'queen' in title_lower or 'dealer' in title_lower:
        cat = "Tycoon"
    elif 'builder' in title_lower or 'city' in title_lower or 'colony' in title_lower or 'farm' in title_lower:
        cat = "Simulation"
    elif 'zombie' in title_lower or 'ninja' in title_lower or 'shooter' in title_lower or 'war' in title_lower:
        cat = "Action"
    elif 'racing' in title_lower or 'race' in title_lower:
        cat = "Racing"
    elif 'puzzle' in title_lower or 'maze' in title_lower or 'crunch' in title_lower or 'solitaire' in title_lower or 'chess' in title_lower:
        cat = "Puzzle"
    elif 'life' in title_lower or 'spa' in title_lower or 'blogger' in title_lower or 'influencer' in title_lower:
        cat = "Lifestyle"
    elif '3d' in title_lower or 'drift' in title_lower or 'flight' in title_lower:
        cat = "3D"
        
    games.append({
        "slug": title.lower().replace(" ", "-").replace(":", ""),
        "title": title,
        "description": f"Experience the professional gameplay of {title}.",
        "short_description": f"Play {title} now!",
        "thumbnail": img,
        "categories": [cat],
        "url": "https://playcanv.as/p/2OlkUaxF/",
        "rating": 4.0 + (i % 10) * 0.1,
        "developer": "PlayGams Studio"
    })

hero1 = re.findall(r'<a class="fp-tile size-hero fp-hero-tile" aria-label="([^"]+)".*?<img class="fp-tile-img" src="([^"]+)"', content)
for title, img in hero1:
    if title not in [g['title'] for g in games]:
        games.append({
            "slug": title.lower().replace(" ", "-").replace(":", ""),
            "title": title,
            "description": f"Experience the professional gameplay of {title}.",
            "short_description": f"Play {title} now!",
            "thumbnail": img,
            "categories": ["Business"],
            "url": "https://playcanv.as/p/2OlkUaxF/",
            "rating": 4.9,
            "developer": "PlayGams Studio"
        })

hero2 = re.findall(r'<div class="fp-tile size-hero fp-hero-tile" aria-label="([^"]+)".*?<img class="fp-tile-img" src="([^"]+)"', content)
for title, img in hero2:
    if title not in [g['title'] for g in games]:
        games.append({
            "slug": title.lower().replace(" ", "-").replace(":", ""),
            "title": title,
            "description": f"Experience the professional gameplay of {title}.",
            "short_description": f"Play {title} now!",
            "thumbnail": img,
            "categories": ["Sports"],
            "url": "https://playcanv.as/p/2OlkUaxF/",
            "rating": 4.8,
            "developer": "PlayGams Studio"
        })


out = {
  "api_version": "1.0",
  "total_games": len(games),
  "last_updated": "2026-06-09",
  "games": games
}

with open('/root/playgamio/html/games.json', 'w') as f:
    json.dump(out, f, indent=2)

print(f"Generated {len(games)} games!")
