d = {}

n = 'fdasdsadsaaddasdasasd'

for l in n:
    if l.isalpha():
        d[l] = d.get(l, 0) + 1
        # if l in d:
        #     d[l] += 1
        # else:
        #     d[l] = 1
    else:
        print(f'{l} - Не является буков!')
print(d)

workers = {
    'employer1': {'name': 'Jhon', 'salary': 7500},
    'employer2': {'name': 'Emma', 'salary': 8000},
    'employer3': {'name': 'Brad', 'salary': 500}
}

for worker in workers:
    if workers[worker]['name'] == 'Brad':
        workers[worker]['salary'] = 8500
        break
print(workers)

supermarket = {
    "milk": {"quantity": 20, "price": 1.19},
    "biscuits": {"quantity": 32, "price": 1.45},
    "butter": {"quantity": 20, "price": 2.29},
    "cheese": {"quantity": 15, "price": 1.90},
    "bread": {"quantity": 15, "price": 2.59},
    "cookies": {"quantity": 20, "price": 4.99},
    "yogurt": {"quantity": 18, "price": 3.65},
    "apples": {"quantity": 35, "price": 3.15},
    "oranges": {"quantity": 40, "price": 0.99},
    "bananas": {"quantity": 23, "price": 1.29}
}

s = 0

for item in supermarket:
    q = supermarket[item]["quantity"]
    p = supermarket[item]["price"]
    s += q*p


print(s)