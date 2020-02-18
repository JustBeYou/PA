from math import sqrt

def ipotenuza(a, b):
    return sqrt(a**2 + b**2)

b = int(input("b = "))

for a in range(1, b):
    if ipotenuza(a, b).is_integer():
        print (a, b, int(ipotenuza(a, b)))
