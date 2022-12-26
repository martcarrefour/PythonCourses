# put your python code here
n = 10
q = 0
# n = 10
# для i в 11 - 20
# для j в 2 - (11**0.5)+1
# если i % j - встречаем хотя бы еще один делитель для числа

for i in range(n+1, n*2):
    k = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            k = False

    if k:
        q += 1

print(q)



