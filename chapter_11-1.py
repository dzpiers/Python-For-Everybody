import re

fhand = open('mbox-short.txt')
match = input('Enter a regular expression:')
total = list()
for line in fhand:
    line = line.rstrip()
    matches = re.findall(match, line)
    if len(matches) > 0:
        total.append(matches)
        x = len(total)

print('mbox-short.txt had', x, 'lines that matched', match)
