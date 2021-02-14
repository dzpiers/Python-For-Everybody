def head(t):
    return t[1:]

def tail(t):
    return t[:-1]

def chop(t):
    a = head(t)
    b = tail(a)
    return b

lol = [1, 2, 3, 4, 5]
h = head(lol)
t = tail(lol)
c = chop(lol)
print(h)
print(t)
print(c)
