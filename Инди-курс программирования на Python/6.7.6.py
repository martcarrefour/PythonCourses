d = {}
d1 = {}
n = 'abc'
n1 = 'cba'

for l in n:
    if l.isalpha():
        d[l] = d.get(l, 0) + 1

for j in n1:
    if j.isalpha():
        d1[j] = d1.get(j, 0) + 1

for i in d:
    print(d[i], d1[i])
    print(d, d1)
    if d[i] != d1[i]:
        print('NO')
        break
else:
    print('YES')
