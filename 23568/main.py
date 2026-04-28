s = open('24_23568.txt').readline()
for c in '123456789':
    s = s.replace(c, '0')
start = None
indst = None
mx = 0
lns = 0
indmx = 0
mxs = None
for i in range(len(s)):
    c = s[i]
    if c.isalpha():
        if start is None or c != start:
            start = c
            indst = i
            continue
        if start == c:
            lns = i - indst + 1
            if lns > mx:
                mx = lns
                mxs = s[indst:i]
                indmx = indst
            indst = i

print(indmx, mxs)