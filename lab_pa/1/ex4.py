n = int(input("n = "))

crestere_max = 0
zi           = 0

val1 = float(input("ziua 1 = "))
i    = 1
while i < n:
    val2 = float(input("ziua {} = ".format(i + 1)))

    if val2 - val1 > crestere_max:
        crestere_max = val2 - val1
        zi           = i

    val1 = val2
    i += 1

if crestere_max == 0:
    print ("nu exista crestere")
else:
    print ("cresterea maxima a fost intre zilele {} si {} cu valoarea {:.3f}".format(zi, zi + 1, crestere_max))
