def replace(text: str, old: str, new: str = ''):
    mas = [new if i == old else i for i in text]
    return ''.join(mas)


print(replace('Нет', 'т'))
print(replace('Bella Ciao', 'a'))
print(replace('nobody; i myself farewell analysis', 'l', 'z'))
print(replace('commend me to my kind lord meaning', 'M', 'w'))


def make_header(string: str, size: int = 1) -> str:
    return f'<h{size}>{string}</h{size}>'


print(make_header('Hello!'))


def create_matrix(size: int = 3, up_fill: int = 0, down_fill: int = 0) -> list:
    """Создание квадратной матрицы"""
    a = []
    for i in range(size):
        b = []
        for j in range(size):
            b.append(0)
        a.append(b)

    for i in range(size):
        for j in range(size):
            if i == j:
                a[i][j] = i + 1
            elif i < j:
                a[i][j] = up_fill
            else:
                a[i][j] = down_fill

    for i in range(size):
        for j in range(size):
            print(a[i][j], end=' ')
        print()

    return a

create_matrix(5,12,15)
