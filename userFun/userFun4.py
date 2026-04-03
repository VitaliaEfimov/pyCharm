import math

def convert_to_celsius(temp):
    return (5 / 9) * (temp - 32) # Функция возвращает значение

def convert_grade(grade):
    if grade >= 90:
        return 5
    elif grade >= 80:
        return 4
    elif grade >= 70:
        return 3
    elif grade >= 60:
        return 2
    else:
        return 1 # Функция с условиями

def get_none():
    a = 1 # Если ничего не возвращаем по умолчанию возвращается None

def compute_hypotenuse(a, b):
    c = (a ** 2 + b ** 2) ** 0.5
    return c

def get_distance(x1, y1, x2, y2):
    return compute_hypotenuse(x1 - x2, y1 - y2)

def sum_digits(n):
    result = 0
    while n > 0:
        result += n % 10
        n //= 10
    return result

def compute_average(numbers):
    return sum(numbers) / len(numbers)

def get_sum(x, y, z):
    return x + y + z
    print('Сумма равна', x + y + z) # После return далее ничего не выполняется


def quick_merge(list1, list2):
    result = []

    p1 = 0  # указатель на первый элемент списка list1
    p2 = 0  # указатель на первый элемент списка list2

    while p1 < len(list1) and p2 < len(list2):  # пока не закончился какой-нибудь из списков
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1

    if p1 < len(list1):  # прицепление остатка
        result += list1[p1:]
    else:  # иначе прицепляем остаток другого списка
        result += list2[p2:]

    return result

print(convert_to_celsius(40))
print(get_none())

# grade = int(input('Введите вашу отметку по 100-балльной системе: '))
grade = 100
print(convert_grade(grade))

print(compute_hypotenuse(3, 4))
print(compute_hypotenuse(5, 12))
print(compute_hypotenuse(1, 1))
print(math.hypot(1, 1))

print(sum_digits(1234)) # 10
numbers = [1, 3, 5, 1, 6, 8, 10, 2]
print(compute_average(numbers)) # 4.5 Вычисляем и выводим среднее значение элементов списка

print(get_sum(1, 2, 3)) # 12

list1 = [3, 10, 11, 12, 47, 57, 58, 63, 77, 79, 80, 95]
list2 = [0, 11, 12, 20, 24, 26, 47, 48, 53, 65, 70, 81, 84, 84, 90]
list3 = quick_merge(list1, list2)
print(list3) # [0, 3, 10, 11, 11, 12, 12, 20, 24, 26, 47, 47, 48, 53, 57, 58, 63, 65, 70, 77, 79, 80, 81, 84, 84, 90, 95]
