import urllib.request

url = 'http://data.pr4e.org/romeo.txt'
content = urllib.request.urlopen(url).read()
content = content.decode()

print(content[:3000])
print(len(content))
