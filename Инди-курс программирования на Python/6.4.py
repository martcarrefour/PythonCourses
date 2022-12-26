# sweet = {
#     "id": "0001",
#     "type": "donut",
#     "name": "Cake",
#     "ppu": 0.55,
#     "calories": 125,
# }
#
# sweet.pop('ppu')
# sweet.pop('type')
#
# print(sweet)


# put your python code here
n = 8
c = {}

for key in range(n + 1):
    c[key] = key * key

print(c)

print('------------------')

from string import ascii_lowercase

print(ascii_lowercase)

c = {}
for l in range(len(ascii_lowercase)):
    c[ascii_lowercase[l]] = l + 1

print(c)
