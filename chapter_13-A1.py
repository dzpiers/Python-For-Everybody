from urllib import request
import xml.etree.ElementTree as ET

url = input('Enter location:')
# http://py4e-data.dr-chuck.net/comments_42.xml
print("Retrieving", url)
html = request.urlopen(url)
data = html.read()
print("Retrieved", len(data), "characters")

tree = ET.fromstring(data)
counts = tree.findall('comments/comment')

total = 0
for count in counts:
    total = total + int(count.find('count').text)
print('Count:', len(counts))
print('Sum:', total)
