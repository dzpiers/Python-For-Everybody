fhand = open('mbox-short.txt')
book = {}
for line in fhand:
    words = line.split()
    if len(words) < 2 or words[0] != 'From': continue
    address = words[1]
    address1 = address.split('@')
    handle = address1[1]
    if handle in book:
        book[handle] += 1
    else:
        book[handle] = 1
print(book)
