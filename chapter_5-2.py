smallest = None
largest = None
while True:
    number = input('Enter a number:')
    try:
        num = float(number)
        if largest == None or num > largest:
            largest = num
        if smallest == None or num < smallest:
            smallest = num
    except:
        print('Invalid input')
    if number == 'done':
        print(smallest, largest)
        break

