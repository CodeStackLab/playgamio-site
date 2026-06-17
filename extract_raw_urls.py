import json
import urllib.request
import re
import time

def extract_raw_urls():
    print("Loading games.json...")
    with open('html/games.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    games = data.get('games', [])
    updated = 0
    
    for game in games:
        url = game.get('url', '')
        if url.startswith('https://githubgames.gitlab.io/game/'):
            try:
                # Fetch the wrapper page
                req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req, timeout=10) as response:
                    html = response.read().decode('utf-8', errors='ignore')
                
                # Find iframe src
                match = re.search(r'<iframe[^>]*?src=["\'](.*?)["\']', html, re.IGNORECASE)
                if match:
                    raw_src = match.group(1)
                    if raw_src.startswith('/'):
                        raw_src = "https://githubgames.gitlab.io" + raw_src
                    print(f"Extracted: {game['slug']} -> {raw_src}")
                    game['url'] = raw_src
                    updated += 1
                else:
                    print(f"Failed to find iframe in: {url}")
            except Exception as e:
                print(f"Error fetching {url}: {e}")
            
            time.sleep(0.1) # Be polite
            
    if updated > 0:
        with open('html/games.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
        print(f"Successfully updated {updated} games with raw URLs!")
    else:
        print("No games needed updating.")

if __name__ == "__main__":
    extract_raw_urls()
