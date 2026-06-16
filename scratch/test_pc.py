import urllib.request
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

ids = ['JtL2iqIH', '2OlkUaxF', 'aP0OXqup', '5vuMFZqD', '1zV29R4A', 'bA4A9wQx', '6EsqR1uS', '4wH4o0rW', 'RqJJ9oU9', '3AUKQxP1']

for i in ids:
    url = f"https://playcanv.as/p/{i}/"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, context=ctx) as r:
            print(f"{i}: {r.getcode()}")
    except Exception as e:
        print(f"{i}: Error {e}")
