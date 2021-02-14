hours = input('Enter hours:')
rate = input('Enter rate:')
if float(hours) > 40:
    pay = (40 * float(rate)) + ((float(hours) - 40) * float(rate) * 1.5)
    print('Pay:', pay)
else:
    pay = float(hours) * float(rate)
    print('Pay:', pay)
