name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
text = open(name)

book = dict()

for line in text:
    line.rstrip()
    if not line.startswith("From "): continue
    words = line.split()
    book[words[1]] = book.get(words[1],0)+1

val_order = list()
for k, v in list(book.items()):
    val_order.append((v, k))

val_order.sort(reverse=True)
print(val_order[0][0], val_order[0][1])



