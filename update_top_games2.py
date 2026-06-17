import json
import os
import shutil

games_file = '/root/playgamio/html/games.json'
with open(games_file, 'r') as f:
    data = json.load(f)

# Demote all current 4.9+ games to 4.8
for g in data.get('games', []):
    if g.get('rating', 0) >= 4.9:
        g['rating'] = 4.8

# For Swoop 3D, fix its image back to default thumbnail since it was broken
for g in data.get('games', []):
    if g.get('slug') == 'swoop-3d':
        g.pop('image', None) # remove the broken generated image

target_slugs = {
    'car-drift-racers-2': {
        'rating': 5.0,
        'image': '/assets/img/car_drift_racers_2.png',
        'title': 'Car Drift Racers 2 (Premium)'
    },
    'death-run-3d': {
        'rating': 4.99,
        'image': '/assets/img/death_run_3d.png',
        'title': 'Death Run 3D (Premium)'
    },
    'extreme-off-road-cars-3-cargo': {
        'rating': 4.98,
        'image': '/assets/img/extreme_off_road.png',
        'title': 'Extreme Off Road 3 (Premium)'
    }
}

os.makedirs('/root/playgamio/html/assets/img', exist_ok=True)
try:
    shutil.copy('/root/.gemini/antigravity-ide/brain/8f92bcc2-814e-432e-a599-de97f49c3fb0/car_drift_racers_2_1781679729208.png', '/root/playgamio/html/assets/img/car_drift_racers_2.png')
    shutil.copy('/root/.gemini/antigravity-ide/brain/8f92bcc2-814e-432e-a599-de97f49c3fb0/death_run_3d_1781679746043.png', '/root/playgamio/html/assets/img/death_run_3d.png')
    shutil.copy('/root/.gemini/antigravity-ide/brain/8f92bcc2-814e-432e-a599-de97f49c3fb0/extreme_off_road_cars_3_cargo_1781679757102.png', '/root/playgamio/html/assets/img/extreme_off_road.png')
except Exception as e:
    print(f"Error copying images: {e}")

for g in data.get('games', []):
    if g.get('slug') in target_slugs:
        updates = target_slugs[g.get('slug')]
        for k, v in updates.items():
            g[k] = v

with open(games_file, 'w') as f:
    json.dump(data, f, indent=4)

print("Updated games.json with new top 3 games!")
