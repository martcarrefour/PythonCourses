lst = [2, 1, 1, 1, 1, 1, 2, 2, 2, 2]


def find_duplicate(lst):
    a = set(lst)
    x = []
    for i in lst:
        if i in a:
            a.remove(i)
        else:
            x.append(i)

    result = (sorted(set(x), key=lst.index))
    return result


find_duplicate(lst)


def first_unique_char(s):
    unic_ch = -1
    for i in s:
        if s.count(i) == 1:
            unic_ch = s.index(i)
            return unic_ch

    return unic_ch


print(first_unique_char('abcabc'))

names = [{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]

print('-' * 100)


def format_name_list(names: list[dict]) -> str:
    a = [name['name'] for name in names]
    res = ''
    if len(a) > 2:
        for i in a[:-2]:
            res += f'{i}, '
        else:
            res += f'{a[-2]} и {a[-1]}'
    elif len(a) == 2:
        res += f'{a[-2]} и {a[-1]}'
    elif len(a) == 1:
        res += a[0]

    return res


def format_namelist(lst):
    a = []
    for i in range(len(lst)):
        a.append(lst[i]['name'])
    if len(a) > 1:
        a.append(a.pop(-2) + " и " + a.pop())
    return ', '.join(a)


print(format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}]))
# print(format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}, {'name': 'Homer'}, {'name': 'Marge'}])=='Bart, Lisa, Maggie, Homer и Marge')

print('-' * 100)
import urllib.parse


def get_domain_name(url):
    res = url
    if 'www' in url:
        res = url.split('.')[1]

    else:
        res = url.split('//')[1].split('.')[0]
    return res


print(get_domain_name("http://google.com"))
print(get_domain_name("http://google.co.jp"))
print(get_domain_name("www.xakep.ru"))
print(get_domain_name("https://youtube.com"))
print(get_domain_name("https://www.asos.com"))
print(get_domain_name("http://www.lenovo.com"))

print('-' * 100)


def factorial(n):
    f = 1

    for i in range(2, n + 1):
        f *= i
    return f


print(factorial(10))


def trailing_zeros(n):
    zers = factorial(n)

    c = 0
    while zers % 10 == 0:
        c += 1
        zers //= 10
    return c


print(trailing_zeros(10))
print('-' * 100)


def count_AGTC(dna):
    agtc = 'AGTC'
    c = [dna.count(i) for i in agtc]
    print(tuple(c))
    return (tuple(c))


print(count_AGTC('AGGTC'))
print(count_AGTC('AAAATTT') == (4, 0, 3, 0))

