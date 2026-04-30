
s = open('24_20968.txt').readline()
# Normalize operators
s = s.replace('*', '+')

# What breaks an expression
# 1. Odd numbers
# 2. Numbers starting with leading 0 (zero)
# 3. Two or more ops in a row (*+)

# Split by ops, so only numbers are in segments
s = s.split('+')
mx = 0
ans = []
for c in s:
    # Is this a start of an expression?
    if c == "" or (len(c) > 1 and c[0] == '0') or (int(c)%2 != 0):
        print(c)
        # bad
        # flush
        lns = sum([len(x) for x in ans]) + len(ans)-1
        mx = max(mx, lns)
        #if ans:
            #print(ans)
        ans = []
    else:
        # good
        ans.append(c)
mx = max(mx, sum([len(x) for x in ans]) + len(ans)-1)


print(mx, ans)

print('===================')

from re import *

num = r'([1-9][0-9]*[02468]|[02468])'
reg = rf'{num}([BA]{num})*'     # ← поменяли + на *

s = open('24_20968.txt').readline().replace('*', 'A').replace('+', 'B')

mx = 0
maxs = ""
for i in finditer(reg, s):
    if len(i[0]) > mx:
        # new max
        mx = len(i[0])
        maxs = i[0].replace('A', '*').replace('B', '+')

print(mx, maxs)