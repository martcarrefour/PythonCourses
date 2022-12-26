n,m = 3,4  # 3спортсмена, 3 броска
a = [
    ["B", "W", "B", "W", ],
    ["B", "B", "W", "B", ],
    ["W", "W", "B", "B", ],


]
for i in a:
    print(i)

print('До инверсии-------------')

for i in range(n):
    for j in range(m):
        a[i][j]
        a[i][j] = 'W' if a[i][j] == 'B' else 'B'

print('После-------------')
for i in a:
    print(i)

# put your python code here
# n, m = map(int, input().split())
# a, b = [], []
#
# for i in range(n):
#     a.append(list(input()))
#
# input()
#
# for i in range(n):
#     b.append(list(input()))
#
# for i in range(n):
#     for j in range(m):
#         a[i][j]
#         a[i][j] = 'W' if a[i][j] == 'B' else 'B'
#
# c = 0
#
# for i in range(n):
#     for j in range(m):
#         if a[i][j] != b[i][j]:
#             c += 1
#
# print(c)
#



