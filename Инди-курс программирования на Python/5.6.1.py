q = 0

for i in range(1000, 10000):
    z = 0
    x = i
    while i > 0:
        z += i % 10
        i //= 10
    if z == 20:
        q += x

print(q)
