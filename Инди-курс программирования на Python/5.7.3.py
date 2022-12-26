# put your python code here


n, m = 3, 3
a = [
    [3, 1, 2],
    [1, 3, 4],
    [3, 3, 3]
]

# for i in range(n):
#     a.append(list(map(int, input().split())))

mx = 0
for i in range(n):
    for j in range(m):
        if a[i][j] > mx:
            mx = a[i][j]
            r = i
            c = j

print(mx)
print(r, c)
