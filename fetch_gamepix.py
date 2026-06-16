import json
import urllib.request
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

req = urllib.request.Request("https://games.gamepix.com/games?sid=400", headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req, context=ctx) as response:
        data = json.loads(response.read().decode())
        
        if data.get('status') == 'success':
            gamepix_games = data.get('data', [])
            
            new_games = []
            
            # Map GamePix data to our format
            for i, g in enumerate(gamepix_games[:200]): # Take 200 games
                new_games.append({
                    "slug": g.get("id", f"game-{i}").lower(),
                    "title": g.get("title", f"Game {i}").strip(),
                    "description": g.get("description", "Play this high quality HTML5 game in your browser!"),
                    "short_description": g.get("description", "Awesome HTML5 Game")[:100] + "...",
                    "thumbnail": g.get("thumbnailUrl", ""),
                    "categories": g.get("categories", ["Casual"]),
                    "url": g.get("url", ""),
                    "rating": round(4.0 + (g.get("rkScore", 0) * 0.1), 1),
                    "developer": g.get("author", "GamePix Studio") or "GamePix Studio"
                })
            
            final_data = {
                "api_version": "1.0",
                "total_games": len(new_games),
                "last_updated": "2026-06-05",
                "games": new_games
            }

            with open('/root/playgamio/html/games.json', 'w') as f:
                json.dump(final_data, f, indent=2)
                
            print(f"Successfully added {len(new_games)} high-quality games from GamePix!")
        else:
            print("Failed to get success status from GamePix")
except Exception as e:
    print("Error:", e)
