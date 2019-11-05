sir1 = input()
sir2 = input()

anagrama = True
for c1 in sir1:
    gasit = False
    for i, c2 in enumerate(sir2):
        if c1 == c2:
            gasit = True
            sir2 = sir2[:i] + "" + sir2[i + 1:]
            break
    if not gasit:
        anagrama = False
        break

if anagrama:
    print ("sunt anagrame")
else:
    print ("nu sunt anagrame")
