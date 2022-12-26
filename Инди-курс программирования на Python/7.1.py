str = 'Привет, Старина'


def count_letters(n):
    l = u = 0
    d = [i for i in n]

    for i in d:
        if i.isupper():
            u += 1
        if i.islower():
            l += 1
    print(f'Количество заглавных символов: {u}')
    print(f'Количество строчных символов: {l}')


count_letters(str)


def is_between(name, surname, middlename):
    print(min(surname, middlename))
    print(max(surname, middlename))
    print('True') if min(surname, middlename) <= name <= max(surname, middlename) else print('False')



def square(x):
    print(x**2)

a = square(6)
print(a)

def example():
    print(1)
    return 2