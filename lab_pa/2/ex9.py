prop = input()

oferte = []
start = 0
while True:
    i = prop.find('$', start)
    start = i + 1
    if i == -1:
        break

    i += 1
    num = ""
    while prop[i].isdigit():
        num += prop[i]
        i += 1
    oferte.append(int(num))

print ("Pret initial: {}".format(oferte[0]))
print ("oferte initiala: {}".format(oferte[1]))

if oferte[-1] == oferte[-2]:
    print ("Cele doua persoane s-au inteles la pretul {}".format(oferte[-1]))
else:
    print ("Cele doua persoane nu s-au inteles")
