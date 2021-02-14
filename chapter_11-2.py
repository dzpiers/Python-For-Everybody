import re

fhand = open('mbox-short.txt')
total = list()
for line in fhand:
    line = line.rstrip()
    x = re.findall('^Details:.*rev=([0-9.]+)', line)
    if len(x) > 0:
        for y in x:
            y = float(y)
        total.append(y)
print(sum(total)/len(total))
