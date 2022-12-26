n = 4  # 3спортсмена, 3 броска
a = [
    ["B", "W", "B", "W", ],
    ["B", "B", "W", "B", ],
    ["W", "W", "B", "B", ],
    ["B", "W", "W", "W", ],

]
#
# for i in range(n):
#     a.append(list(input()))

# put your python code here
flag = True
for i in range(n-1):
    for j in range(n-1):
        x = a[i][j]
        if x == a[i][j+1] and x == a[i+1][j] and x == a[i+1][j+1]:
            flag = False

print('Yes') if flag else print('No')


