prop = input()
vocale = "aeiouAEIOU"

alege = input("1. romana -> pasareasca\n2. pasareasca -> romana\n")

new_prop = ""
if alege == '1':
    for c in prop:
        if c in vocale:
            new_prop += c + "p" + c
        else:
            new_prop += c
elif alege == '2':
    i = 0
    while i < len(prop):
        c = prop[i]
        new_prop += c
        if c in vocale:
            i += 3
        else:
            i += 1

print (new_prop)
