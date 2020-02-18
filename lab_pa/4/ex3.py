
def min_max(*args):
    if len(args) == 0:
        return None

    min_value = int(args[0])
    max_value = int(args[0])
    for i in args:
        if not i.is_integer() or i < 0:
            return None
        i = int(i)
        min_value = min(i, min_value)
        max_value = max(i, max_value)
    return min_value, max_value

try:
    with open('numere.txt', 'r') as f:
        numbers = [float(x.strip()) for x in f.read().split()]
except TypeError as e:
    print ("Tipuri invalide")
except:
    print ("Nu s-a putut citi fisierul")
    exit()

result = min_max(*numbers)
if result == None:
    print ("Input invalid")
    exit()
result = result[1] / result[0]
try:
    with open('impartire.txt', 'w') as f:
        f.write(str(result))
except:
    print ("Nu s-a putut scrie")
    exit()
