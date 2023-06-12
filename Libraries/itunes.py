import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit()

res = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])

# print(json.dumps(res.json()), indent=4, sort_keys=True)

data = res.json()
for result in data["results"]:
    print(result["trackName"])
    print(result["artistName"])
    print(result["collectionName"])