from functools import wraps


def decor(func):
    def inner(*args, **kwarg):
        print('start decorator..')
        func(*args, **kwarg)
        print('end decorator..')

    return inner


def text_decor(func):
    def inner(*args, **kwargs):
        print('Hello')
        func(*args, **kwargs)
        print('Goodbye!')

    return inner


@decor
def say(name, age):
    print('hello!', name, age)


say('Dima', 25)


def repeater(func):
    def inner(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)

    return inner


@repeater
def multiply(num1, num2):
    print(num1 * num2)


multiply(2, 7)


def double_it(func):
    @wraps(func)
    def inner(*args, **kwargs):
        return func(*args, *kwargs) * 2

    return inner


def multiply(num1, num2):
    '''
    Some text
    :param num1:
    :param num2:
    :return:
    '''
    return num1 * num2


res = multiply(9, 4)  # произведение 9*4=36, но декоратор double_it удваивает это значение
print(res)
print('-'*10)
multiply = double_it(multiply)
print(multiply(3,4))
print(multiply.__doc__)
