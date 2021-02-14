name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
text = open(name)

book = dict()

for line in text:
    line.rstrip()
    if not line.startswith("From "): continue
    words = line.split()
    book[words[1]] = book.get(words[1],0)+1

key_list = list(book.keys())
val_list = list(book.values())
position = val_list.index(max(val_list))
print(key_list[position], max(val_list))
