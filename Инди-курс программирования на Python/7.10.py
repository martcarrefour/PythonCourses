r = lambda x: x ** 2
print(r(7))

adding_10 = lambda x: x + 10

print(adding_10(5))

starts_with = lambda s: s.startswith('W')

print(starts_with('dsadsa'))

sale_lambda = lambda x: x * 0.9 if x > 50 else x

print(sale_lambda(10))

print('-' * 10)


def color() -> None:
    g = 'sss'

    def grey() -> None:
        nonlocal g
        g = 'grey'
        print(g)

    grey()
    print(g)


color()
print('-' * 10)


def calculate(x: float, y: float, operator: str = 'a') -> None:
    addition = lambda x, y: x + y
    subtraction = lambda x, y: x - y
    division = lambda x, y: x / y if y != 0 else 'На ноль делить нельзя!'
    multiplication = lambda x, y: x * y

    match operator:
        case "a":
            print(addition(x, y))
        case "s":
            print(subtraction(x, y))
        case "d":
            print(division(x, y))
        case "m":
            print(multiplication(x, y))
        case _:
            print('Ошибка. Данной операции не существует')


calculate(2, 5) # Печатает 7.0
calculate(2.2, 15, 'a') # Печатает 17.2
calculate(22, 15, 's') # Печатает 7.0
calculate(2, 3.2, 'm') # Печатает 6.4
calculate(10, 0.4, 'd') # Печатает 25.0
calculate(10, 0, 'd') # Печатает 'На ноль делить нельзя!'
calculate(10, 4, 'w') # Печатает 'Ошибка. Данной операции не существует'