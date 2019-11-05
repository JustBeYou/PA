x = int(input("x = "))
n = int(input("n = "))
p = int(input("p = "))
m = int(input("m = "))

bucati = m // n
rest   = m % n

distanta = 0
for i in range(bucati):
    distanta += x * n
    x -= x * (p / 100)
distanta += x * rest

print ("distanta parcursa este {}".format(distanta))
