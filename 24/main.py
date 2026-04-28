#
# Task 26077 from KEG
#

s = open('24.txt').readline()
for c in '3579':
    s = s.replace(c, '1')
s = s.split('G')
mx = 0
lx = 0
for x in s:
    k = 0
    for i in range(len(x)):
        c = x[i]
        if c == '1':
            k += 1
            if k == 46:
                lx = i # todo check
                break
    if k == 45:
        lx = len(x)
    mx = max(mx, lx)
print(mx +1)

