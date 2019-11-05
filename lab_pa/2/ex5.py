from string import ascii_lowercase, ascii_uppercase

t = input()
k = int(input())

ascii_len = len(ascii_lowercase)
c = ""
for ch in t:
    if ch in ascii_uppercase:
        c += ascii_uppercase[(ascii_uppercase.find(ch) + k) % ascii_len]
    elif ch in ascii_lowercase:
        c += ascii_lowercase[(ascii_lowercase.find(ch) + k) % ascii_len]
    else:
        c += ch

print (c)
