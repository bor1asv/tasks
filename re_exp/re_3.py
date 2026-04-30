s = open('24-213.txt').readline()
from re import*

pat = r'(PNO|NPO)+'
mx = 0
ms = finditer(pat, s)
for m in ms:
    g = m.group()
    mx = max(mx, len(g))
print(mx//3)
