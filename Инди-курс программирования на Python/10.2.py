# Функции-генераторы

def gen():
    for i in [4, 312, 32]:
        yield i


s = gen()

print(next(s))
print(next(s))


def fact_gen(n):
    pr = 1
    for i in range(1, n + 1):
        pr = pr * i

        yield pr


for i in fact_gen(10):
    print(i, end=' ')


def gen_squares(n):
    for i in range(1, n + 1):
        i **= 2

        yield i


s = gen_squares(2)

print('-' * 10)


def gen_fibonacci_numbers(n):
    fib1 = fib2 = 1

    for i in range(n):
        if i == 0 or i == 1:
            yield 1
        else:
            fib1, fib2 = fib2, fib1 + fib2
            yield fib2


for i in gen_fibonacci_numbers(10):
    print(i)

i = range(5)
print('-' * 10)


def my_range_gen(stop: int, start: int = 0, step: int = 1):
    if start > stop or step < 1:
        stop, start = start, stop

    yield start
    if start < stop:
        while start < stop - step:
            start += step
            yield start
    else:

        while start > stop - step:
            start += step
            yield start


for i in my_range_gen(5):
    print(i)
print('-' * 10)
for i in my_range_gen(4, 8):
    print(i)
print('-' * 10)
for i in my_range_gen(4, 8, 2):
    print(i)
print('-' * 10)
for i in my_range_gen(4, 8, 2):
    print(i)
print('-' * 10)
for i in my_range_gen(8, 5, -1):
    print(i)