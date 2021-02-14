fhand = open('mbox-short.txt')
day = {}
for line in fhand:
    words = line.split()
    if len(words) < 2 or words[0] != 'From': continue
    commit = words[2]
    if commit in day:
        day[commit] += 1
    else:
        day[commit] = 1
print(day)
