import json

games_file = 'html/games.json'
with open(games_file, 'r') as f:
    data = json.load(f)

games = data.get('games', [])

seemore_img = "https://images.unsplash.com/photo-1518773553398-650c184e0bb3?auto=format&fit=crop&w=1200&q=80" # Tech/3D looking
astray_img = "https://images.unsplash.com/photo-1506452819137-0422416856b8?auto=format&fit=crop&w=1200&q=80" # Maze/path looking

def add_or_update(slug, title, img, desc):
    found = False
    for game in games:
        if game.get('slug') == slug:
            game['image'] = img
            game['thumbnail'] = img
            game['rating'] = 4.9 # Make it hot
            found = True
            print(f"Updated {slug}")
    if not found:
        print(f"Adding {slug}")
        games.append({
            "slug": slug,
            "title": title,
            "url": "https://playcanvas.com/play/embed/123",  # Placeholder
            "thumbnail": img,
            "image": img,
            "categories": ["3D", "Puzzle", "Action"],
            "rating": 4.9,
            "developer": "PlayGamio",
            "controls": "Keyboard",
            "description": desc,
            "short_description": "Amazing 3D Game"
        })

add_or_update("seemore-3d", "SeeMore 3D", seemore_img, "An incredible 3D visual experience.")
add_or_update("astray-3d-maze", "Astray 3D Maze", astray_img, "Navigate through a complex 3D maze.")

# Sort to ensure hot games are at the top
games_sorted = sorted(games, key=lambda x: x.get('rating', 0), reverse=True)

data['games'] = games_sorted
with open(games_file, 'w') as f:
    json.dump(data, f, indent=4)
print("Games added/updated!")
