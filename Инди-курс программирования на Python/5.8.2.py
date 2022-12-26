n, m = 4, 4
a = []

for i in range(n):
    b = []
    for j in range(m):
        b.append('.')
    a.append(b)

a[1][1] = '*'

for i in a:
    print(*i)
c = 0
for i in range(n):
    for j in range(m):
        print(m%j)

print(c)
for i in a:
    print(*i)
