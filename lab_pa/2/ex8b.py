prop = input()
new_prop = ""

for i, c in enumerate(prop):
    if c in '-, .!?' and prop[i - 1].isalpha():
        new_prop += "p" + prop[i - 1].lower() + c
    else:
        new_prop += c

print (new_prop)
print (new_prop.replace('-', ''))
