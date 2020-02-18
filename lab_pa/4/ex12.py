def cautare(x, L, cmpValori):
    for i, e in reversed(list(enumerate(L))):
        if cmpValori(x, e):
            return i
    return None

n = int(input('n = '))
v = []
for i in range(n):
    x = int(input('v[{}] = '.format(i)))
    v.append(x)

while len(v) != 0:
    if len(v) == 1:
        v = []
        break

    i = cautare(v[0], v, lambda x, y: x == y)
    if i == len(v) - 1:
        v.pop(0)
        v.pop(len(v) - 1)
    else:
        break

if len(v) == 0:
    print ("da")
else:
    print ("nu")
