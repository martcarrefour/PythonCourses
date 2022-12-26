# put your python code here


n, m = 3, 3  # 3спортсмена, 3 броска
a = [
    [6, 2, 7],
    [1, 2, 8],
    [1, 2, 8]

]

# put your python code here
mx = 0
winner_id = int
for i in range(n):
    for j in range(m):
        if a[i][j] > mx:
            mx = a[i][j]
            winner_id = i
            r = j

mx_count = 0
winners = []
print(f'mx: {mx}')

for i in range(n):
    if mx in a[i]:
        mx_count += 1
        winners.append(a[i])
    else:
        winners.append([])

print(f'mx_count: {mx_count}')
print(f'winners: {winners}')

if mx_count > 1:
    max_sum = 0
    winner_id = 0
    for i in range(n):
        if sum(winners[i]) > max_sum:
            max_sum = sum(winners[i])
            winner_id = i
        elif max_sum > 0 and max_sum == sum(winners[i]):
            winner_id = i - 1
            break

    print(f'max_sum: {max_sum}')
    print(f'winner_id: {winner_id}')
    print(f'{winner_id}')


else:
    print(winner_id)
