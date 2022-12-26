# Цифры проверяемой последовательности нумеруются справа налево.
# Цифры, оказавшиеся на нечётных местах, остаются без изменений.
# Цифры, стоящие на чётных местах, умножаются на 2.
# Если в результате такого умножения возникает число больше 9, оно уменьшается на значение 9
# Все полученные в результате преобразования 16 цифр складываются. Если сумма кратна 10, то исходные данные верны.


n = '3942682966937054'

n = [int(i) for i in n[::-1]]
a = []
for index, value in enumerate(n, 1):
    if index % 2 == 0:
        value *= 2
        if value > 9:
            value -= 9
        a.append(value)
    else:
        a.append(value)

print('True') if sum(a) % 10 == 0 else print('False')

words = ['feel', 'graduate', 'movie', 'fashionable', 'bacon',
         'drop', 'produce', 'acquisition', 'cheap', 'strength',
         'master', 'perception', 'noise', 'strange', 'am']

words_with_position = [(i, v) for v, i in enumerate(words, 1)]
print(words_with_position)
