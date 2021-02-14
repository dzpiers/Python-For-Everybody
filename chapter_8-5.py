fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    # print('Debug:', words)
    if len(words) < 2 or words[0] != 'From': continue
    count = count + 1
    print(words[1])
print('There were', count, 'lines starting with "From"')
