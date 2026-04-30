import re

s = open('k7a-3.txt').readline()

# \d == class of digits
# \w == class of letters
# [abcd] == class of a,b,c,d
# + == one or more
# * == zero or more

pat = r'[ABEF]+'
ms = re.finditer(pat, s)

mgl = 0
mg = ''
for m in ms:
    g = m.group()
    if len(g) > mgl:
        mgl = len(g)
        mg = g

print(mgl, mg)
