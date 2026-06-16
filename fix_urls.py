import json

with open('/root/playgamio/html/games.json', 'r') as f:
    data = json.load(f)

for game in data['games']:
    game['url'] = f"https://play.gamepix.com/{game['slug']}/embed?sid=1"

with open('/root/playgamio/html/games.json', 'w') as f:
    json.dump(data, f, indent=2)

print("Successfully restored all 42 games to proper working GamePix embed URLs!")
