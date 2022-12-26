def count_args(*args) -> int:
    '''Данная функция должна возвращать количество переданных ей на вход аргументов'''
    return len(args) or 0


print(count_args())


def check_sum(*args: int) -> str:
    print('verification passed') if sum(args) >= 50 else print('not enough')


check_sum(10, 23)
check_sum(321, 23)


def multiply(*args: int) -> int:
    '''Данная функция должна находить произведение
    всех переданных значений и возвращать
    его в качестве результата'''
    n = 1
    for i in args:
        print(n)
        n = n * i
    return n


print(multiply(12, 10))
print('-' * 50)


def only_one_positive(*args: int) -> bool:
    '''принимает произвольное количество числовых аргументов
    и возвращает True, когда из всех переданных
    значений только одно положительное, в противном случае верните False'''

    c = 0
    for i in args:
        if i > 0:
            c += 1
    return True if c == 1 else False


print(only_one_positive(0, 2, 1))

print('-' * 50)


def print_goods(*args: str):
    goods = []
    for i in args:
        if isinstance(i, str) and i != '':
            goods.append(i)

    if goods:
        for id, item in enumerate(goods, 1):
            print(f'{id}. {item}')
    else:
        print('Нет товаров')


print(print_goods(1, True, 'Грушечка', '', 'Pineapple'))
print_goods([], {}, 1, 2)

print('-' * 50)


def info_kwargs(**kwargs):
    """ Функция info_kwargs должна распечатать именованные
    аргументы в каждой новой строке в виде пары <Ключ> = <Значения>,
    причем ключи должны следовать в алфавитном порядке.
    """
    for i in sorted(kwargs):
        print(f'{i} = {kwargs[i]}')


info_kwargs(first_name="John", last_name="Doe", age=33)

print('-' * 50)


def create_actor(**kwargs):
    '''принимает произвольное количество именованных
    аргументов и возвращает словарь с характеристиками актера.'''
    info = {
        'name': 'Райан',
        'surname': 'Рейнольдс',
        'age': 46
    }

    info.update(kwargs)

    return info


print(create_actor(movies=['Дедпул', 'Главный герой']))
