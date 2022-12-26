# Генератор списка
a = [i ** 2 for i in range(1, 6)]

# Выражения-генераторы - Можно обойти только 1 раз! Не храним в памяти, а вызываем с помощью next
b = (i ** 2 for i in range(1, 6))
print(next(b))
print(next(b))

# c = list(range(10000000000)) -! Переполнение памяти
# c = [i for i in range(10000000000)] -! Переполнение памяти
c = (i for i in range(10000000000))  # Можем обходить
print(c)

# for i in c:
#     print(i)

from random import randint

d = (randint(1, 20) for i in range(7))
print(sorted(d))

d = (i ** 2 for i in range(1, 6))
print(9 in d, 4 in d)

d = (i ** 2 for i in range(1, 6))
print(4 in d, 9 in d)

from_10_to_20 = (i for i in range(10, 21))
# print(list(from_10_to_20))
print(next(from_10_to_20))
print(next(from_10_to_20))
print(next(from_10_to_20))

# выведите все оставшиеся
for value in from_10_to_20:
    print(value)

print('-' * 10)

week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

days = ((i, week[(i + 4) % 7]) for i in range(1, 366))

[print(next(days)) for i in range(77)]
