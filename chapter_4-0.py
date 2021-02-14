import random

for i in range(10):
    x = random.random()
    print(x)

print(random.randint(5, 10))

t = [1, 2, 3]
print(random.choice(t))

tot = 0
for i in [5, 4, 3, 2, 1] :
    tot = tot + 1
print(tot)
