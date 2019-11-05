def verifica_nume(nume):
    return nume.count('-') <= 1 and nume.replace('-', '').isalpha() and len(nume) >= 3 and nume[0].isupper()

nume = input().strip()
nume = nume.split()

ok = len(nume) == 2 and verifica_nume(nume[0])
prenume = nume[1]
pozitie = -1
for i, c in enumerate(prenume):
    if c.isupper():
        if prenume[i - 1] == '-':
            if pozitie != -1:
                ok = False
            else:
                pozitie = i - 1
            break

prenume = [prenume[:pozitie], prenume[pozitie + 1:]]
ok = ok and verifica_nume(prenume[0]) and (len(prenume) == 1 or verifica_nume(prenume[1]))

if ok:
    print ("Nume corect")
else:
    print ("Nume incorect")
