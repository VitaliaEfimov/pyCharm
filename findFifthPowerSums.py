import time

start_time = time.time()

def find_fifth_power_sums(limit=150):
    solutions = []
    total = 0

    # Для каждого значения 'e' будем проверять суммы четвертых степеней остальных переменных
    for e in range(1, limit):
        fifth_e = e ** 5
        seen_powers = set()

        # Проверяем комбинацию всех возможных пар сумм четвертых степеней
        for a in range(1, min(e, limit)):
            a_pow = a ** 5

            for b in range(a + 1, min(e, limit)):  # Начинаем от a+1, чтобы избежать дублирования
                ab_sum = a_pow + b ** 5

                for c in range(b + 1, min(e, limit)):
                    abc_sum = ab_sum + c ** 5

                    for d in range(c + 1, min(e, limit)):
                        sum_of_powers = abc_sum + d ** 5

                        if sum_of_powers == fifth_e:
                            total += 1
                            solutions.append((a, b, c, d, e))  # Добавляем решение в список
                        end_time = time.time()

                        execution_time = end_time - start_time
                        h = int(execution_time // 3600)
                        m = int((execution_time % 3600) // 60)
                        s = int(execution_time % 60)
                        mil = round((execution_time * 1000) % 1000)

                        print(f'a:  {a}, b:  {b}, c:  {c}, d:  {d}, e:  {e}, time: {h}:{m}:{s}:{mil}')
    return total, solutions


limit = 150
total_solutions, solution_list = find_fifth_power_sums(limit)

print("Общее количество натуральных решений:", total_solutions)
if len(solution_list) > 0:
    print("Решения:")
    for sol in solution_list:
        print(sol)
else:
    print("Нет решений.")