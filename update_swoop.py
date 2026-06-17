import json

games_file = 'html/games.json'
with open(games_file, 'r') as f:
    data = json.load(f)

games = data.get('games', [])

featured_image = "https://images.unsplash.com/photo-1436491865332-7a61a109cc05?auto=format&fit=crop&w=1200&q=80" 

found = False
for game in games:
    if game.get('slug') == 'swoop-3d' or 'swoop' in game.get('slug', '').lower():
        game['image'] = featured_image
        game['thumbnail'] = featured_image
        found = True
        print(f"Updated {game.get('slug')} with featured image.")

if not found:
    print("Could not find swoop-3d, adding it...")
    new_game = {
        "slug": "swoop-3d",
        "title": "Swoop 3D",
        "url": "https://playcanvas.com/play/embed/123456",  # Placeholder URL
        "thumbnail": featured_image,
        "image": featured_image,
        "categories": ["3D", "Action", "Simulation"],
        "rating": 4.6,
        "developer": "PlayCanvas",
        "controls": "Keyboard & Mouse",
        "description": "A beautiful 3D flying game.",
        "short_description": "Fly like a bird in 3D"
    }
    games.append(new_game)

with open(games_file, 'w') as f:
    json.dump(data, f, indent=4)
