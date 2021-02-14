word_dict = {}
fhand = open("words.txt")
for line in fhand:
    words = line.split()
    for word in words:
        word_dict[word] = ""
print(word_dict)

print('creative' in word_dict)
