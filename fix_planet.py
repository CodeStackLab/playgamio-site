import json

games_file = 'html/games.json'
with open(games_file, 'r') as f:
    data = json.load(f)

games = data.get('games', [])

planet_img = "https://images.unsplash.com/photo-1614730321146-b6fa6a46bcb4?auto=format&fit=crop&w=1200&q=80" # Planet/City 3D looking image

found = False
for game in games:
    if game.get('slug') == 'planet-city-3d' or 'planet-city' in game.get('slug', '').lower():
        print(f"Found {game['slug']}. Current thumbnail: {game.get('thumbnail')} | Current image: {game.get('image')}")
        game['image'] = planet_img
        game['thumbnail'] = planet_img
        found = True

if not found:
    print("Could not find planet-city-3d. Adding it...")
    games.append({
        "slug": "planet-city-3d",
        "title": "Planet City 3D",
        "url": "https://playcanvas.com/play/embed/12345",
        "thumbnail": planet_img,
        "image": planet_img,
        "categories": ["3D", "Simulation", "Tycoon"],
        "rating": 4.8,
        "developer": "PlayGamio",
        "controls": "Keyboard & Mouse",
        "description": "Build your own 3D planet city.",
        "short_description": "Build a 3D city"
    })

with open(games_file, 'w') as f:
    json.dump(data, f, indent=4)
print("Updated planet-city-3d image!")
