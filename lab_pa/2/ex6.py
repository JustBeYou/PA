prop = input().split()

suma = 0
for i, c in enumerate(prop):
    if len(c) < 3: continue
    if c[:3] == "RON" and (len(c) == 3 or not c[3].isalpha()):
        suma += int(prop[i - 1])

print (suma)
