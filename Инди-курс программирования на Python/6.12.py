u_input = [
    'Дили: navalny',
    'Дили: realdonaldtrump',
    'Били: navalny',
    'Вили: realdonaldtrump',
    'Вили: realdonaldtrump',
    'Били: joebiden',
    'Дили: joebiden',
]

# while a != 'конец':
#     u_input.append(a)
#     a = input()

users = {'Дили': set(), 'Били': set(), 'Вили': set()}

# Подсчёт уникальных комментариев
for m in u_input:
    users[m.split(': ')[0]].add(m.split(': ')[1])

print(users)

l = {}
print(users.items())
for i, v in users.items():
    if v:
        l[len(v)] = i
    else:
        l[0] = i
print(l)
# Вывод остортированных комметариев
for i, v in sorted(l.items(), reverse=True):
    print(f'Количество уникальных комментаторов у {v} - {i}')
