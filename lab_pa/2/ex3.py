prop = input()
s = input()
t = input()

new_prop = ""
start = 0
while True:
    i = prop.find(s, start)
    if i == -1:
        new_prop += prop[start:]
        break
    new_prop += prop[start:i]

    if prop[i:i + len(s)] == s and (i == 0 or not prop[i - 1].isalpha()) and (i == len(prop) - len(s) or not prop[i + len(s)].isalpha()):
        new_prop += t
    else:
        new_prop += s
    start = i + len(s)


print (new_prop)
