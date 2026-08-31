def matrix(n=1, m=None, value=0):
    if m is None:
        m = n

    return [[value] * m for _ in range(n)]

print(matrix(3)) # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print(matrix()) # [[0]]
print(matrix(3, 4, 9)) # [[9, 9, 9, 9], [9, 9, 9, 9], [9, 9, 9, 9]]
print(matrix(2, 5)) # [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
print(matrix(4)) # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
print(matrix(3, 2, 5)) # [[5, 5], [5, 5], [5, 5]]
print(matrix(3, 1)) # [[0], [0], [0]]