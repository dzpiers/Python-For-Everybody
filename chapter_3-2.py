try:
    hours = input('Enter hours:')
    type(float(hours)) == float
    rate = input('Enter rate:')
    type(float(rate)) == float
    pay = float(hours) * float(rate)
    print('Pay:', pay)
except:
    print('Error, please enter a numeric input')
