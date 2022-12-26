n, x = 12, 6
a = []

for i in range(1, n + 1):
    b = []
    for j in range(1, n + 1):
        b.append(i * j)
    a.append(b)
    print()

c = 0
for i in range(n):
    for j in range(n):
        if a[i][j] == x:
            c += 1


for i in a:
    print(i)

print(c)