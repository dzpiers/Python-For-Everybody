ihand = input('Enter file:')
fhand = open(ihand)
sorted_list = []
for line in fhand:
    words = line.split()
    for word in words:
        if word in sorted_list:
            continue
        sorted_list.append(word)
sorted_list.sort()
print(sorted_list)
