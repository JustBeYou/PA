with open('cuvinte.txt', 'r') as f:
    L = [x.strip() for x in f.read().split() if x.strip() != '']

a=sorted(L, reverse=True)
print (a)

a=sorted(L, key = lambda x: (len(x), x))
print (a)


a=sorted(L, key = lambda x: len(x))
print (a)

