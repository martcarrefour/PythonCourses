# models = [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
#           {'make': 'Mi Max', 'model': 2, 'color': 'Gold'},
#           {'make': 'Samsung', 'model': 7, 'color': 'Blue'},
#           {'make': 'Apple', 'model': 10, 'color': 'Silver'},
#           {'make': 'Oppo', 'model': 9, 'color': 'Red'},
#           {'make': 'Huawei', 'model': 4, 'color': 'Grey'},
#           {'make': 'Honor', 'model': 3, 'color': 'Black'}]
#
# for i in sorted(models, key=lambda x: x['color']):
#     print(f'Производитель: {i["make"]}, модель: {i["model"]}, цвет: {i["color"]}')
#


m = ['Sony PlayStation 5: 46000', 'Телевизор QLED Samsung QE65Q60TAU: 87090', 'Смартфон Samsung Galaxy A11: 10000',
     'Планшет Samsung Galaxy Tab S6: 26600']

for item in sorted(m, key=lambda x: int(x.split(': ')[1]), reverse=True):
    print(item.split(':')[0])

m = ['Леонардо Ди Каприо', 'Джонни Депп', 'Леонардо Ди Каприо', 'Леонардо Ди Каприо', 'Джонни Депп', 'Мэтт Деймон']

m = list(sorted(m, key=lambda x: m.count(x), reverse=True))
print(f'{m[0]}, {m.count(m[0])}')
print(f'{m[-1]}, {m.count(m[-1])}')
print('=' * 10)
m = {'Дууек,': [2, 3], 'Дааалл,': [2, 3]}


for i in sorted(m.items(), key=lambda x: (-sum(x[1]) / len(x[1]), x[0])):
    print(i[0], sum(i[1]) / len(i[1]))
