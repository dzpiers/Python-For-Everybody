filename = input('Enter a file name:')
fileopen = open(filename)
count = 0
line2 = None
total = 0
count1 = 0

for line in fileopen:
    count = count + 1
    if line.startswith('X-DSPAM-Confidence:'):
        count1 = count1 + 1
        line1 = line.rstrip()
        line2 = line1[19:]
        line2 = float(line2)
        total = total + line2

print('Average spam confidence:', total/count1)



