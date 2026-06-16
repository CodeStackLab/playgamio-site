import json
import random

working_games = [
    "https://gamesnacks.com/embed/games/bouncemasters",
    "https://gamesnacks.com/embed/games/lumberjack",
    "https://gamesnacks.com/embed/games/omnomrun",
    "https://gamesnacks.com/embed/games/cuttherope",
    "https://gamesnacks.com/embed/games/stackbounce",
    "https://gamesnacks.com/embed/games/towercrash",
    "https://gamesnacks.com/embed/games/elementblocks",
    "https://gamesnacks.com/embed/games/candybubble",
    "https://gamesnacks.com/embed/games/poolclub",
    "https://gamesnacks.com/embed/games/onetconnectclassic",
    "https://gamesnacks.com/embed/games/colorpixelartclassic",
    "https://gamesnacks.com/embed/games/jewelblocks",
    "https://gamesnacks.com/embed/games/mahjongclassic"
]

with open('/root/playgamio/html/games.json', 'r') as f:
    data = json.load(f)

for i, game in enumerate(data['games']):
    game['url'] = working_games[i % len(working_games)]

with open('/root/playgamio/html/games.json', 'w') as f:
    json.dump(data, f, indent=2)

print("Updated games.json with real GameSnacks embed URLs")
