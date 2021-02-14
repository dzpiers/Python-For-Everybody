total = 0
count = 0
while True:
    number = input('Enter a number:')
    try:
        float(number)
        total = total + float(number)
        count = count + 1
    except:
        print('Invalid input')
    if number == 'done':
        print(total, count, total/count)
        break

