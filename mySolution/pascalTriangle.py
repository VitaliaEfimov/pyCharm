def pascal(n):
    if n == 0:
        return []
    if n == 1:
        return [[1]]

    triangle = pascal(n - 1)
    prev_row = triangle[-1]
    new_row = [1] + [prev_row[i] + prev_row[i + 1] for i in range(len(prev_row) - 1)] + [1]
    triangle.append(new_row)

    return triangle


n = int(input())
for r in pascal(n):
    print(*r)