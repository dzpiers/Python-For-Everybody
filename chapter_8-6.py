numbers = []

while True:
    a = input('Enter a number:')
    if a == 'done':
        break
    try:
        b = float(a)
        numbers.append(b)
    except:
        print('Invalid input')

numbers.sort()
print('Minimum:', numbers[0])
print('Maximum:', numbers[-1])

print('Minimum:', min(numbers))
print('Maximum:', max(numbers))


