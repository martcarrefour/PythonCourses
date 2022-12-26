def main_func(value):
    def inner():
        print('Hello', value)

    return inner


b = main_func('Dmitriy')
d = main_func('Misha')
print(b())
print(d())
print('-' * 10)


def adder(value):
    def inner(a):
        return value + a

    return inner


a = adder(3)
print(a(4))

print('-' * 10)


def counter():
    count = 0

    def inner():
        nonlocal count
        count += 1
        return count

    return inner


c = counter()
print(c())
print(c())
print(c())

print('-' * 10)


def multiply(n: int):
    def inner(a: int):
        return n * a

    return inner


f_2 = multiply(2)

print(f_2(5))
