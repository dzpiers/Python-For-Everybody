filename = input('Enter a file name:')
fileopen = open(filename)

for line in fileopen:
    print(line.upper())
