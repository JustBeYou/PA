n = int(input("n = "))

max1 = None
max2 = None
for i in range(n):
    x = int(input("numarul {} = ".format(i)))

    if max1 == None:
        max1 = x
    elif max2 == None and x != max1:
        max2 = x
        max1, max2 = max(max1, max2), min(max1, max2)

    if max1 != None and max2 != None:
        if x > max1:
            max2 = max1
            max1 = x
        elif x > max2 and x != max1:
            max2 = x

if max1 == None or max2 == None:
    print ("imposibil")
else:
    print ("{}, {}".format(max1, max2))

