a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

delta = b ** 2 - 4 * a * c

if delta < 0:
    print ("Ec nu are radacini reale")
elif delta == 0:
    print ("x = {}".format(-b/(2*a)))
else:
    print ("x1 = {}, x2 = {}".format((-b + delta ** 0.5) / (2 * a), (-b - delta ** 0.5) / (2 * a)))
