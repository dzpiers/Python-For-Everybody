import urllib.request
import json

url = input('Enter URL: ')
# http://py4e-data.dr-chuck.net/comments_42.json
# http://py4e-data.dr-chuck.net/comments_1091120.json

connection = urllib.request.urlopen(url)
data = connection.read().decode()
info = json.loads(data)
print("Retrieving", url)
print("Retrieved", len(data), "characters")
print('Count:', len(info['comments']))

total = 0
for item in info['comments']:
    total += int(item['count'])
print('Sum:', total)
