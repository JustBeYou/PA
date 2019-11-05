text = "Python was conceived in the late 1980s as a successor to the ABC language. Python 2.0, released in 2000, introduced features like list comprehensions and a garbage collection system capable of collecting reference cycles. Python 3.0, released in 2008, was a major revision of the language that is not completely backward-compatible, and much Python 2 code does not run unmodified on Python 3. Due to concern about the amount of code written for Python 2, support for Python 2.7 (the last release in the 2.x series) was extended to 2020. Language developer Guido van Rossum shouldered sole responsibility for the project until July 2018 but now shares his leadership as a member of a five-person steering council."

props = []
start = 0
for i, c in enumerate(text):
    if c.isupper() and i >= 2 and text[i - 2] == '.':
        props.append(text[start:i - 1])
        start = i
props.append(text[start:])

print ('\n'.join(props))
