fhand = open('mbox-short.txt')
book = {}
for line in fhand:
    words = line.split()
    if len(words) < 2 or words[0] != 'From': continue
    address = words[1]
    if address in book:
        book[address] += 1
    else:
        book[address] = 1
print(book)
