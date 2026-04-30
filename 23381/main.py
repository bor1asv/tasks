s = open('24_23381.txt').readline()
for c in '02468':
   s = s.replace(c, ' ')
for c in '13579':
    s = s.replace(c, '1')
s = s.split()
mx = 0
for x in s:
    if x[0].isalpha():
        letter = x[0]
        fl = True
        for a in x:
            if a != letter:
                fl = False
                break
        if fl == True:
            mx = max(mx, len(x))
print(mx + 2)