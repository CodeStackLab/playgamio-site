import json
import os
import shutil

games_file = '/root/playgamio/html/games.json'
with open(games_file, 'r') as f:
    data = json.load(f)

for g in data.get('games', []):
    if g.get('rating', 0) >= 4.9:
        g['rating'] = 4.8

target_slugs = {
    'highway-racer-3d': {
        'rating': 5.0,
        'image': '/assets/img/highway_racer_3d_1781678735704.png',
        'title': 'Highway Racer 3D (Premium)'
    },
    'swoop-3d': {
        'rating': 4.99,
        'image': '/assets/img/swoop_3d_1781678745169.png',
        'title': 'Swoop 3D (Premium)'
    },
    'astray-3d-maze': {
        'rating': 4.98,
        'title': 'Astray 3D Maze (Premium)'
    }
}

# Copy the images to a public dir so the frontend can load them
os.makedirs('/root/playgamio/html/assets/img', exist_ok=True)
try:
    shutil.copy('/root/.gemini/antigravity-ide/brain/8f92bcc2-814e-432e-a599-de97f49c3fb0/highway_racer_3d_1781678735704.png', '/root/playgamio/html/assets/img/highway_racer_3d_1781678735704.png')
    shutil.copy('/root/.gemini/antigravity-ide/brain/8f92bcc2-814e-432e-a599-de97f49c3fb0/swoop_3d_1781678745169.png', '/root/playgamio/html/assets/img/swoop_3d_1781678745169.png')
except Exception as e:
    print(f"Error copying images: {e}")

for g in data.get('games', []):
    if g.get('slug') in target_slugs:
        updates = target_slugs[g.get('slug')]
        for k, v in updates.items():
            g[k] = v

with open(games_file, 'w') as f:
    json.dump(data, f, indent=4)

print("Updated games.json successfully!")
