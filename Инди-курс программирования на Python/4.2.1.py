n = 4
a = [1, 2, 3, 4]
m = 5
b = [10, 11, 12, 13]

a.sort()
b.sort()
a.reverse()
b.reverse()

print(a)
print(b)
c = 0
i = 0
while len(a) > 0 and len(b) > 0:
    if abs(a[i] - b[i]) > 1:
        if a[i] > b[i]:
            a = a[1:]
        else:
            b = b[1:]
    else:
        c += 1
        a, b = a[1:], b[1:]
print(c)
