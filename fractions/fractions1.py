"""
✅ Рациональное число – это число, которое можно представить в виде дроби m/n. m и n соответственно, числитель
и знаменатель, которые имеют целочисленное значение, при этом знаменатель не равен нулю.

✅ Тип данных Fraction из модуля fractions представляет собой обыкновенную дробь с заданными числителем и знаменателем.

✅ Создать Fraction число можно несколькими способами:

из целых чисел, передав значения числителя и знаменателя дроби,
из строки на основании десятичного представления;
из строки на основании обыкновенной дроби;
из числа с плавающей точкой (не рекомендуется).
✅ Fraction числа можно сравнивать между собой точно так же, как и любые другие числа.

✅ С Fraction числами работают все привычные операции: сложение, вычитание, умножение, деление, возведение в степень.

✅ Для получения числителя и знаменателя Fraction числа используются свойства numerator и denominator.

✅ Метод as_integer_ratio() возвращает кортеж, состоящий из числителя и знаменателя данного Fraction числа.

✅ Метод limit_denominator() возвращает самую близкую к данному числу рациональную дробь, чей знаменатель не превосходит переданного аргумента. Метод позволяет получить очень точные рациональные приближения иррациональных чисел.
"""
from fractions import Fraction
from math import *
import math

num1 = Fraction(3, 4)     # 3 - числитель, 4 - знаменатель
num2 = Fraction('0.55')
num3 = Fraction('1/9')

print(num1, num2, num3) # 3/4 11/20 1/9

num1 = Fraction(0.34) # Не рекомендуется использовать
num2 = Fraction('0.34')

print(num1) # 6124895493223875/18014398509481984
print(num2) # 17/50
print()

num1 = Fraction(5, 10)
num2 = Fraction('75/100')
num3 = Fraction('0.25')

print(num1, num2, num3) # 1/2 3/4 1/4 автоматически происходит сокращение числителя и знаменателя дроби
print()

num1 = Fraction(5, 1)        # 5/1 = 5
num2 = Fraction(23, 23)      # 23/23 = 1

print(num1, num2) # 5 1

num1 = Fraction(1, 2)        # 1/2
num2 = Fraction(15, 30)      # 15/30=1/2
num3 = Fraction(3, 5)        # 3/5
num4 = Fraction(5, 3)        # 5/3
num5 = 1
num6 = 0.8


print(num1 == num2) # True
print(num1 != num4) # True
print(num2 > num3) # False
print(num4 <= num1) # True
print(num1 < num5) # False
print(num6 > num4) # False
print()

num1 = Fraction('1/10')
num2 = Fraction('2/3')

print(num1 + num2) # 23/30
print(num1 - num2) # -17/30
print(num1 * num2) # 1/15
print(num1 / num2) # 3/20
print()

num = Fraction('3/8')

print(num + 1) # 11/8
print(num - 1) # -5/8
print(num * 2) # 3/4
print(num ** 4) # 81/4096 операции с целыми числами, выполнять операции с float не рекомендуется
print()

num1 = Fraction('3/8')
num2 = Fraction('1/2')

print(num1 ** num2) # 0.6123724356957945 при возведении в степень Fraction может вывести вещественный результат
print()

num1 = Fraction('1.44')
num2 = Fraction('0.523')

print(sqrt(num1)) # 1.2 результатом работы функций модуля math являются float числа
print(sin(num2)) # 0.4994813555186418
print(log(num1 + num2)) # 0.6744739152943241
print()

num = Fraction('5/16')

print('Числитель дроби равен:', num.numerator) # Числитель дроби равен: 5
print('Знаменатель дроби равен:', num.denominator) # Знаменатель дроби равен: 16
print()

num = Fraction('-5/16')

print(num.as_integer_ratio()) # (-5, 16)
print()

print('PI =', math.pi) # PI = 3.141592653589793

num = Fraction(str(math.pi))

print('No limit =', num) # No limit = 3141592653589793/1000000000000000

for d in [1, 5,  50, 90, 100, 500, 1000000]:
    limited = num.limit_denominator(d)
    print(limited)
"""
3
16/5
22/7
267/85
311/99
355/113
3126535/995207
"""
print()

from fractions import Fraction as F

num1 = F('1/5') + F('3/2')
num2 = F('1/4') * F('2/5')

print(num1) # 17/10
print(num2) # 1/10
print()

from decimal import Decimal

num1 = Decimal('12.5')
num2 = F(19, 3)
# нельзя совершать арифметические операции (+, -, *, /) между типами Decimal и Fraction
# print(num1 + num2) # TypeError: unsupported operand type(s) for +: 'decimal.Decimal' and 'Fraction'
num = F('1 / 9') # пробелы добавлять можно в Python 3.12 и выше
print(num)