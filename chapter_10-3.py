import string
fhand = open('romeo.txt')
counts = dict()
letters_dict = dict()
for line in fhand:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        letters = list(word)
        for letter in letters:
            letters_dict[letter] = letters_dict.get(letter, 0) + 1

# Sort the dictionary by value
lst = list()
for key, val in list(letters_dict.items()):
    lst.append((val, key))

lst.sort(reverse=True)

for key, val in lst:
    print(key, val)
