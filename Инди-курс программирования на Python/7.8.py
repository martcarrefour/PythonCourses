def print_to(n: int) -> None:
    if n == 0:
        return False
    print_to(n - 1)
    print(n)


print_to(5)


def print_from(n: int) -> None:
    if n == 0:
        return False
    print(n)
    print_from(n - 1)


print_from(5)

print('-' * 10)


def double_fact(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n > 2:
        return double_fact(n - 2) * n


print(double_fact(8))

print('-' * 10)


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        return fib(n - 1) + fib(n - 2)


print(fib(7))

print('-' * 10)


def tribonacci(n):
    if n == 0 or n == 1:
        return 0
    if n == 2:
        return 1
    if n > 2:
        return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)


print(tribonacci(8))
print('-' * 10)


def get_combin(n: int, k: int) -> int:
    if k == 0 or k == n:
        return 1
    if 0 < k < n:
        return get_combin(n - 1, k) + get_combin(n - 1, k - 1)


print(get_combin(6, 3))

print('-' * 10)


def ackermann(m: int, n: int) -> int:
    if m == 0:
        return n + 1
    if m > 0 and n == 0:
        return ackermann(m - 1, 1)
    if m > 0 and n > 0:
        return ackermann(m - 1, ackermann(m, n - 1))


print(ackermann(3, 5))

print('-' * 10)

n = [1, 2, 3]


def list_sum_recursive(n) -> int:
    if not n:
        return 0
    if len(n) == 1:
        return n[0]
    return n[0] + list_sum_recursive(n[1:])


print(list_sum_recursive(n))

print('flatten' + '-' * 10)
n = [1, [2, 3, [4]], 5]


def flatten(n):
    if not n:
        return n
    if isinstance(n[0], list):
        return flatten(n[0]) + flatten(n[1:])
    return n[:1] + flatten(n[1:])


print(flatten(n))
print('(((' + '-' * 10)
n = 'fdsfdsfdssddsfdvcs'


def hooks(n: str):
    if len(n) == 1 or len(n) == 2:
        return n
    return n[0] + '(' + hooks(n[1:-1]) + ')' + n[-1]


print(hooks(n))
print('-' * 10)


def power(x: float, n: float) -> float:
    if n == 0:
        return 1
    if n < 0:
        return 1 / power(x, -n)
    if n % 2 == 0:
        return power(x, n // 2) * power(x, n // 2)
    else:
        return power(x, n - 1) * x


print(power(5, -3))

print('-' * 10)
# nested = {'Germany': {'berlin': 7},
#           'Europe': {'italy': {'Rome': 3}},
#           'USA': {'washington': 1, 'New York': 4}}
#

# flatten_dict(nested) => {'Germany_berlin': 7,
#                          'Europe_italy_Rome': 3,
#                          'USA_washington': 1,
#                          'USA_New York': 4}
nested = {'Germany': {'berlin': 7}}


def flatten_dict(d: dict) -> dict:
    if not d:
        return d
    for k, v in enumerate(d):
        if isinstance(d[v], dict):
            return flatten_dict(v)


print(flatten_dict(nested))
