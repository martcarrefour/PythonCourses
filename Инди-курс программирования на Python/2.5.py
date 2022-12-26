# a, b, c = 1, 2, 3
# a, b, c = 0, 255, 10
a, b, c = 154, 73, 55
colors = [a, b, c]
res = '#'

for _ in range(3):
    res += hex(input()).lstrip('0x').zfill(2).upper()
