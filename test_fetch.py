import urllib.request, json
req = urllib.request.Request("https://www.freetogame.com/api/games", headers={'User-Agent': 'Mozilla/5.0'})
try:
    resp = urllib.request.urlopen(req)
    print("Success!", resp.getcode())
except Exception as e:
    print("Error:", e)
