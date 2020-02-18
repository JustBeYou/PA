from math import pi

def lungime_arie_cerc(r):
    return 2 * r * pi, r ** 2 * pi

r = float(input("r = "))
print (lungime_arie_cerc(r))
