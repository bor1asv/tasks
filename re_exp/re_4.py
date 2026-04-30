s = open('24-215.txt').readline()
from re import*
pat = r'([ABC][123])+'
ms = finditer(pat, s)
mx = 0
mxind = 0
for m in ms:
    g = m.group()
    ind = m.span()
    if len(g) > mx:
        mx = len(g)
        mxind = ind[0]
print(mx//2, mxind)
