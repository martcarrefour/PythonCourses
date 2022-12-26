# l = 6
# n = [22, 4, 55, 15, 55, 6]
#
# for i in range(1, l):
#     temp = n[i]
#     j = i - 1
#     while j >= 0 and temp < n[j]:
#         j -= 1
#
#
#
# print(n)


l = 6
n = [22, 4, 55, 15, 55, 6]

for i in range(1, l):
    temp = n[i]
    j = i - 1
    while j >= 0 and temp < n[j]:
        n[j + 1] = n[j]
        j = j - 1
    n[j + 1] = temp
print(n)
