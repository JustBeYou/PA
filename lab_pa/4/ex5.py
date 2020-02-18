def negative_pozitive(l):
    neg = []
    poz = []
    for i in l:
        if i > 0:
            poz.append(i)
        elif i < 0:
            poz.append(i)
    return neg, poz

fisier = input("fisier = ")
with open(fisier, 'r') as f
