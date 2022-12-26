
m = 'Python is best I love python'.split()
a = ''

z = []
for i in range(len(m)):
    if m[i].lower() not in a.lower():
        a += m[i]
        z.append(m[i])

print(*z)
