def find_divisors(n):
    if n <= 0:
        raise ValueError("Число должно быть положительным")

    divisors = []
    i = 1
    while i * i <= n:
        print('перебор', i)
        if n % i == 0:
            print('доавбляем', i)
            divisors.append(i)
            if i != n // i:  # Избегаем дублирования квадратного корня
                print('получаем верхний', i, ' ', n // i)
                divisors.append(n // i)
        i += 1

    return sorted(divisors)

print(find_divisors(100))
# for i in range(2, 100):
#     lst = find_divisors(i)
#     print(i, ' делители: ', lst, ('не простое', 'простое') [len(lst) == 2])
