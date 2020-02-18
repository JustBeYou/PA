from math import sqrt
def prime():
    yield 2
    i = 3
    while True:
        has_div = False
        for d in range(2, int(sqrt(i)) + 1):
            if i % d == 0:
                has_div = True
                break
        if not has_div:
            yield i
        i += 2

n = int(input("n = "))

for i, v in enumerate(prime()):
    print (v)
    if i == n - 1:
        break

