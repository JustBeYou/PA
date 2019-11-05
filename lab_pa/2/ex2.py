prop = input()
prop = prop.split()
prop = [x[0].upper() + x[1:] for x in prop]
print (' '.join(prop))
