n = int(input("n = "))

# cel mai mic
solutie = 0
gasit   = False

for i in range(1, 9 + 1):
    x   = n
    while x:
        if x % 10 == i:
            solutie *= 10
            solutie += i

            if not gasit:
                y = n
                while y:
                    if y % 10 == 0:
                        solutie *= 10
                    y //= 10
                gasit = True
        x //= 10


print ("cel mai mic numar {}".format(solutie))

# cel mai mare
solutie = 0

for i in range(9, -1, -1):
    x   = n
    cnt = 0
    while x:
        if x % 10 == i:
            cnt += 1
        x //= 10

    for j in range(cnt):
        solutie *= 10
        solutie += i

print ("cel mai mare nunmar {}".format(solutie))
