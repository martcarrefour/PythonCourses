n = 7

m = [8, 5, 3, 1, 4, 7, 9]
q = 0
for i in range(n-1):
    for i in range(n-1):
        if m[i] > m[i + 1]:
            q+=1
            m[i], m[i + 1] = m[i + 1], m[i]


print(m)
print(q)