def counter(target, word):
    count = 0
    for letter in word:
        if letter == target:
            count = count + 1
    print(count)

counter('a', 'Mikasa')
