def citire():
    n = int(input("n = "))
    v = []
    for i in range(n):
        x = int(input("v[{}] = ".format(i)))
        v.append(x)

    return v

def afisare(v):
    print (' '.join([str(x) for x in v]))

def valpoz(v):
    poz = []
    for i in v:
        if i > 0:
            poz.append(i)
    return poz
def semn(v):
    for i in range(v):
        v[i] = -v[i]
    return v
