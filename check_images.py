import json
import urllib.request

with open('html/games.json') as f:
    data = json.load(f)

broken = []
for g in data.get('games', []):
    img = g.get('image') or g.get('thumbnail')
    if not img:
        broken.append(g.get('title'))
        continue
    if img.startswith('/'):
        img = 'http://localhost' + img
    try:
        req = urllib.request.Request(img, method='HEAD')
        with urllib.request.urlopen(req, timeout=5) as response:
            if response.status >= 400:
                broken.append(g.get('title'))
    except Exception:
        broken.append(g.get('title'))

print("Broken images found:", len(broken))
for b in broken:
    print("- " + b)
