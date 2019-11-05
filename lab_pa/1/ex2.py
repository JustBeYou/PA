from math import gcd

l1 = int(input("l1 = "))
l2 = int(input("l2 = "))

sz = gcd(l1, l2)
nr = (l1 / sz) * (l2 / sz)

print ("{} placi de {} cm".format(int(nr), sz))
