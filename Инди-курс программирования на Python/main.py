t = 7
n = [-8, -19, 0, 8, 8, 2, 8]
count = [0] * 201

f = []
for i in n:
    count[i + 100] += 1

for i in range(201):
    if count[i] > 0:
        print((str(i - 100) + ' ') * count[i], end='')

# print(' '.join(map(str, f)))
