vector = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],
          [10, 11, 12],
          [13, 14, 15],
          [16, 17, 18]]

a = [n for row in vector for n in row]


# flattened = []
# for row in vector:
#     for n in row:
#         flattened.append(n)
# print(flattened)


print(a)

