filename = input('Enter a file name:')
if filename == 'na na boo boo':
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
    exit()
try:
    fileopen = open(filename)
    count = 0
    for line in fileopen:
        count = count + 1
    print('There are', count, 'subject lines in', filename)

except:
    print('File cannot be opened:', filename)
