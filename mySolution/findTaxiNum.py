import time

def find_taxi_numbers(count, t):
    found_numbers = []  # Список найденных интересных чисел
    cube_dict = {}  # Словарь для хранения чисел, представимых как сумма двух кубов

    # Ограничимся поиском до определенного предела (для повышения эффективности)
    limit = 10000

    # Внешний цикл перебирает первое число
    for a in range(1, limit):
        a_cubed = a ** 3

        # Внутренний цикл перебирает второе число
        for b in range(a, limit):
            b_cubed = b ** 3
            total = a_cubed + b_cubed

            end_time = time.time()
            execution_time = end_time - t
            h = int(execution_time // 3600)
            m = int((execution_time % 3600) // 60)
            s = int(execution_time % 60)
            mil = round((execution_time * 1000) % 1000)

            print(f'a:  {a}, b:  {b}, total:  {total}, time: {h}:{m}:{s}:{mil}')

            # Проверяем, можно ли записать это число другим способом
            if total not in cube_dict:
                cube_dict[total] = [(a, b)]
            else:
                cube_dict[total].append((a, b))
                # Если нашли новое представление, добавляем число в список
                if len(cube_dict[total]) >= 2:
                    found_numbers.append(total)
                    if len(found_numbers) >= count:
                        break
        if len(found_numbers) >= count:
            break

    return sorted(found_numbers[:count])


# Найдем первые 5 чисел, соответствующих условию
t = time.time()
result = find_taxi_numbers(100, t)
print(result)