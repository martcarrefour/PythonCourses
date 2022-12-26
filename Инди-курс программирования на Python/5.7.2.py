# put your python code here
n = 5
a = []

# b = []
# for i in range(n):
#     c = []
#     for j in range(n):
#         c.append(0)
#     b.append(c)
#
# b[0][0] = 1
# for i in b:
#     print(i)
#
# a = b

for i in range(n):
    a.append( list(map(int,input().split())))
s = 0

for i in range(n):
    for j in range(n):
        if a[i][j] == 1:
            # print(i, j)
            k = 2 - i
            y = 2 - j
            s = abs(k + y)
            # print(f'K+Y {k + y}')
            # print(i + (2 - i))
            # while j != 2 or i != 2:
            #     #     for b in a:
            #     #             print(b)
            #     if j < 2:
            #         a[i][j] = 0
            #         j += 1
            #         s += 1
            #         a[i][j] = 1
            #     elif j > 2:
            #         a[i][j] = 0
            #         j -= 1
            #         s += 1
            #         a[i][j] = 1
            #     elif i < 2:
            #         a[i][j] = 0
            #         i += 1
            #         s += 1
            #         a[i][j] = 1
            #     elif i > 2:
            #         a[i][j] = 0
            #         i -= 1
            #         s += 1
            #         a[i][j] = 1

print(s)

# for i in a:
#    print(i)


numbers = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
s = 0
s += numbers.pop()

n = [0, 12, 7]
for i in n:
    s += numbers.pop(i)

print(numbers)
print(s)