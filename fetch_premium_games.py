import urllib.request
import json
import ssl
import sys

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://catalog.api.gamedistribution.com/api/v2.0/rss/All/?format=json&amount=42"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

try:
    response = urllib.request.urlopen(req, context=ctx)
    data = json.loads(response.read().decode('utf-8'))
except Exception as e:
    print("Error fetching GameDistribution API:", e)
    sys.exit(1)

playgamio_games = []

for g in data:
    try:
        # Determine best thumbnail (we want 512x512 or closest)
        thumb = g['Asset'][0] if g.get('Asset') else "https://via.placeholder.com/512"
        
        playgamio_games.append({
            "title": g.get("Title", "Unknown Game"),
            "slug": g.get("Md5", "unknown"),
            "url": g.get("Url", ""),
            "image": thumb,
            "description": g.get("Description", ""),
            "short_description": g.get("Description", "")[:80] + "...",
            "controls": g.get("Instructions", "Mouse / Keyboard"),
            "developer": "GameDistribution",
            "release_date": "Updated 2024",
            "categories": g.get("Category", ["Action"]),
            "tags": g.get("Tag", ["game"])
        })
    except Exception as e:
        print("Skipping a game due to error:", e)

output = {
    "games": playgamio_games
}

with open('/root/playgamio/html/games.json', 'w') as f:
    json.dump(output, f, indent=4)

print(f"Successfully generated {len(playgamio_games)} premium games!")
