import json
import os

games_file = 'html/games.json'

with open(games_file, 'r') as f:
    data = json.load(f)

games = data.get('games', [])

# High quality hero images for top 3 games
hd_hero_images = [
    "https://images.unsplash.com/photo-1542751371-adc38448a05e?auto=format&fit=crop&w=1600&q=80",
    "https://images.unsplash.com/photo-1552820728-8b83bb6b773f?auto=format&fit=crop&w=1600&q=80",
    "https://images.unsplash.com/photo-1538481199705-c710c4e965fc?auto=format&fit=crop&w=1600&q=80"
]

default_img = "https://images.unsplash.com/photo-1614680376573-df3480f0c6ff?auto=format&fit=crop&w=800&q=80"

games_sorted = sorted(games, key=lambda x: x.get('rating', 0), reverse=True)

for i, game in enumerate(games_sorted):
    if i < 3:
        game['image'] = hd_hero_images[i]
        game['thumbnail'] = hd_hero_images[i]
    else:
        if not game.get('thumbnail') and not game.get('image'):
            game['thumbnail'] = default_img
            game['image'] = default_img

# Write back
data['games'] = games
with open(games_file, 'w') as f:
    json.dump(data, f, indent=4)

print("Images fixed!")
