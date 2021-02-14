import re

fhand = open('regex_sum_1091115.txt')
total = list()
for line in fhand:
    line = line.rstrip()
    x = re.findall('([0-9]+)', line)
    if len(x) > 0:
        for y in x:
            total.append(int(y))
print(sum(total))
