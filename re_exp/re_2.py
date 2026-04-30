s = 'FCCAFCFBFBFCAFEABFFFECFCCDEEBECAEABEDEBDCC'
s = open('k7a-6.txt').readline()
from re import*
pat = r'[^AE]+'
ms = finditer(pat, s)
mx = 0
gmx = ''
for m in ms:
    g = m.group()
    if len(g) > mx:
        mx = len(g)
        gmx = g
print(gmx, mx)
