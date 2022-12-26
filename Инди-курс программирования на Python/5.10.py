a = [0 for i in range(7)]
print(a)
print('------------')
n = 3
m = 6
b = ['#' * m for i in range(n)]

for i in b:
    print(i)
print('------------')
c = [(i, j) for i in 'abc' for j in [1, 2, 3]]

for i in c:
    print(i)

print('------------')
d = [i ** 3 for i in range(1, 11)]
for i in d:
    print(i)
print('------------')
x = '1 23 32 123 3213 645'.split()

z = [int(i) for i in x]
print(z)
print('------------')
n = 4
a = [i for i in range(1, n + 1) if n % i == 0]
print(a)
print('------------')
n = 7
# n = int(input())
a = [i for i in range(n, n * n + 1) if i % 2 != 0]
print(a)
print('------------')

a, b = 3, 1

c = [i ** 2 for i in range(a, b + 1)] if a <= b else [i ** 3 for i in range(a, b - 1, -1)]
print(c)

print('------------')
st = 'Create a list of the first letters of every word in this string'

n = [i[0] for i in st.split()]
print(n)

print('------------')

phrase = 'Take only the words that start with t in this sentence'

c = [i for i in phrase.split() if i[0] == 't' or i[0] == 'T']

print(c)
