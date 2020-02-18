from re import findall

def citeste(nume_fisier):
    with open(nume_fisier, 'r') as f:
        s = f.read()
    return s

def determina_ip(nume_fisier):
    s = citeste(nume_fisier)
    found = findall(r'PING ([a-z0-9_]+\.[a-z0-9_]+) \(([0-9\.]+)\)', s)
    if len(found) == 0:
        return None
    found = found[0]

    return found[0], found[1]

def nr_pachete(nume_fisier):
    s = citeste(nume_fisier)
    found = findall(r'[0-9]+ bytes from [0-9\.]+: icmp_seq', s)
    return len(found)

def verificare_timp(nume_fisier):
    s = citeste(nume_fisier)
    found = findall(r'time=([0-9\.]+) ms', s)
    if len(found) == 0:
        raise Exception("Nu s-au gasit pachete")

    found = [float(x) for x in found]
    timp_min = min(found)
    timp_max = max(found)
    timp_med = sum(found) / nr_pachete(nume_fisier)

    found = findall(r'min/avg/max/stddev = ([0-9\.]+)/([0-9\.]+)/([0-9\.]+)', s)
    found = found[0]

    if int(timp_min * 1000) != int(float(found[0]) * 1000) or \
       int(timp_max * 1000) != int(float(found[2]) * 1000) or \
       int(timp_med * 1000) != int(float(found[1]) * 1000):
           raise Exception("Timpii difera")

    return timp_min, timp_max, timp_med

ip, dns = determina_ip('ping.in')
print ("Domain: {}".format(dns))
print ("IP: {}".format(ip))
pachete = nr_pachete('ping.in')
print ("Total pachete: {}".format(pachete))
timp_min, timp_max, timp_med = verificare_timp('ping.in')
print ("Timp minim: {:.3f}".format(timp_min))
print ("Timp maxim: {:.3f}".format(timp_max))
print ("Timp mediu: {:.3f}".format(timp_med))

