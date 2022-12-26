# n = int(input())
n = 3
a = []
s = 0
for i in range(n):
    b = []
    for j in range(n * i + 1, n * (i + 1) + 1):
        b.append(j)
    a.append(b)

for i in a:
    print(i)

for i in range(n):
    for j in range(n):
        if i == j:
            s += a[i][j]


#     [1,2,3], # i = 1, j = 1-4   2*i = 2 i*i = 1 i*n=3 1
#     [4,5,6], # i = 2, j = 4-7   2*i = 3 i*i = 4 i*n=6 4
#     [7,8,9]  # i = 3  j = 7-10  2*i = 6 i*i = 9 i*n=9 7
#
#     3*0+1 = 1
#     3*1+1 = 4
#     3*2+1 = 7
#
#
# for j in range(n):
#     b = []
#     for i in range(n * j + 1, n * (j + 1) + 1):
#         b.append(i)
#     a.append(b)
#
# for i in a:
#     print(i)
#
#     [1,2,3], # i = 1, j = 1-4   2*i = 2 i*i = 1 i*n=3 1
#     [4,5,6], # i = 2, j = 4-7   2*i = 3 i*i = 4 i*n=6 4
#     [7,8,9]  # i = 3  j = 7-10  2*i = 6 i*i = 9 i*n=9 7
