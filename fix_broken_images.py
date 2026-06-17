import json
import os
import shutil

games_file = '/root/playgamio/html/games.json'
with open(games_file, 'r') as f:
    data = json.load(f)

# The generated images mapping
target_slugs = {
    'planet-city-3d': '/assets/img/planet_city.png',
    'astray-3d-maze': '/assets/img/astray.png',
    'seemore-3d': '/assets/img/seemore.png',
    'ball-pool-3d': '/assets/img/ball_pool.png',
    'spider-solitaire': '/assets/img/spider_solitaire.png'
}

# Copy files
try:
    shutil.copy('/root/.gemini/antigravity-ide/brain/8f92bcc2-814e-432e-a599-de97f49c3fb0/planet_city_3d_1781680537740.png', '/root/playgamio/html/assets/img/planet_city.png')
    shutil.copy('/root/.gemini/antigravity-ide/brain/8f92bcc2-814e-432e-a599-de97f49c3fb0/astray_3d_maze_1781680548760.png', '/root/playgamio/html/assets/img/astray.png')
    shutil.copy('/root/.gemini/antigravity-ide/brain/8f92bcc2-814e-432e-a599-de97f49c3fb0/seemore_3d_1781680567456.png', '/root/playgamio/html/assets/img/seemore.png')
    shutil.copy('/root/.gemini/antigravity-ide/brain/8f92bcc2-814e-432e-a599-de97f49c3fb0/ball_pool_3d_1781680577466.png', '/root/playgamio/html/assets/img/ball_pool.png')
    shutil.copy('/root/.gemini/antigravity-ide/brain/8f92bcc2-814e-432e-a599-de97f49c3fb0/spider_solitaire_1781680593648.png', '/root/playgamio/html/assets/img/spider_solitaire.png')
except Exception as e:
    print(f"Error copying images: {e}")

for g in data.get('games', []):
    if g.get('slug') in target_slugs:
        g['image'] = target_slugs[g.get('slug')]
        g['thumbnail'] = target_slugs[g.get('slug')]

with open(games_file, 'w') as f:
    json.dump(data, f, indent=4)

print("Updated missing images!")
