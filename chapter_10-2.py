name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
text = open(name)

hour = dict()

for line in text:
    line.rstrip()
    if not line.startswith("From "): continue
    words = line.split()
    time = words[5]
    time = time.split(':')
    hour[time[0]] = hour.get(time[0],0)+1
print(hour)

lst = list()
for k, v in list(hour.items()):
    lst.append((k,v))

lst.sort()
for a in lst:
    print(a[0], a[1])
