import json

with open('/root/playgamio/html/games.json', 'r') as f:
    data = json.load(f)

for game in data['games']:
    if game['slug'] == '2048-classic':
        game['url'] = 'https://cyberzhg.github.io/2048/'

with open('/root/playgamio/html/games.json', 'w') as f:
    json.dump(data, f, indent=2)

print("Updated 2048 URL to an embeddable one!")
