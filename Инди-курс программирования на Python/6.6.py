n = 4
d = {}
v = []

for i in range(n):
    a = input()
    if a not in d.values():
        d[i] = a
        v.append(a)
        print('OK')
    else:
        a += str(v.count(a))
        d[i] = a
        print(a)

d = {1: '321', 2: '321', 3: '3211'}
