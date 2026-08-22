"""
✅ Тип данных Decimal – это класс из стандартного модуля decimal. Он представляет собой число с плавающей точкой и используется для точных вычислений.

✅ Для типа данных Decimal можно настроить:

точность выполнения операций в количестве десятичных знаков;
режимы округления;
режимы обработки исключительных ситуаций (деление на ноль, переполнение и так далее).
✅ Создать Decimal число можно из обычного целого числа (int) или из строки (str). Возможно создание из числа с плавающей точкой (float), однако делать этого не рекомендуется, так как в Decimal попадет уже неправильно округленное число.

✅ С Decimal числами работают все привычные операции: сложение, вычитание, умножение, деление, возведение в степень.

✅ Тип данных Decimal содержит некоторые встроенные математические методы, возвращающие значения Decimal.

Метод-Описание
sqrt()-вычисляет квадратный корень из Decimal числа
exp()-возвращает e^x для Decimal числа
ln()-вычисляет натуральный логарифм (по основанию e) Decimal числа
log10() вычисляет десятичный логарифм (по основанию10) Decimal числа

✅ Метод as_tuple() возвращает кортеж из3 элементов:

sign – знак числа (0 для положительного числа и 1 для отрицательного числа);
digits – цифры числа;
exponent – значение экспоненты (количество цифр после точки, умноженное на −1).
✅ Базовые параметры Decimal можно посмотреть в его контексте, выполнив функцию getcontext().

✅ Параметр контекста prec (от англ. precision – точность) предназначен для управления точностью.

✅ Метод quantize() позволяет округлять числа Decimal. В качестве первого аргумента принимает объект Decimal, указывающий на формат округления. В качестве второго аргумента принимает стратегию округления:

ROUND_CEILING – округление в направлении бесконечности (Infinity);
ROUND_FLOOR – округляет в направлении минус бесконечности (- Infinity);
ROUND_DOWN – округление в направлении нуля;
ROUND_HALF_EVEN – округление до ближайшего четного числа, число 6.5 округлится не до 7, а до 6;
ROUND_HALF_DOWN – округление до ближайшего нуля;
ROUND_UP – округление от нуля;
ROUND_05UP – округление от нуля (если последняя цифра после округления до нуля была бы 0 или 5, в противном случае – к нулю).
✅ Сравнение float и Decimal чисел:

Характеристика / тип	              float	     Decimal
Реализация	                      аппаратная	программная
Размер                              64 бит	    не ограничен
Основание экспоненты                  2              10
Скорость	                         ✔️	             ❌
Настраиваемость	                     ❌	             ✔️
Для финансов и бизнеса	             ❌	             ✔️
Для симуляций, визуализаций и игр	 ✔️	             ❌
Для высокоточных вычислений	         ❌	             ✔️
"""
from decimal import *
from math import *

print(["NO", "YES"][0.3 == 0.3]) # YES
num = 0.1 + 0.1 + 0.1
eps = 0.000000001           # точность сравнения

if abs(num - 0.3) < eps:    # число num отличается от числа 0.3 менее чем 0.000000001
    print('YES')
else:
    print('NO')
print(["NO", "YES"][(num) == 0.3]) # NO
print()

d1 = Decimal(1)
d2 = Decimal(567)
d3 = Decimal(-93)
d4 = Decimal('12345')
d5 = Decimal('52.198')

print(d1, d2, d3, d4, d5, sep='\n') # Правильно создавать объекты Decimal из int, str в которой написано целое значение
# или число с плавающей точкой
print()

num = Decimal(0.1) # 0.1000000000000000055511151231257827021181583404541015625

print(num) # Из float создавать класс Decimal не рекомендуется - создастся не правильно округленное число
print()
num1 = Decimal('5.2')
num2 = Decimal('2.3')

print(num1 + num2) # 7.5
print(num1 - num2) # 2.9
print(num1 * num2) # 11.96
print(num1 / num2) # 2.260869565217391304347826087
print(num1 // num2) # 2
print(num1 ** num2) # 44.34122533787992500412791298
print()

num1 = Decimal('1.44')
num2 = Decimal('0.523')

print(sqrt(num1)) # 1.2
print(sin(num2)) # 0.4994813555186418
print(log(num1 + num2)) # 0.6744739152943241
print()
num = Decimal('10.0')

print(num.sqrt()) # 3.162277660168379331998893544 вычисляет квадратный корень из Decimal числа
print(num.exp()) # 22026.46579480671651695790065 возвращает e^x для Decimal числа
print(num.ln()) # 2.302585092994045684017991455 вычисляет натуральный логарифм (по основанию e) Decimal числа
print(num.log10()) # 1 вычисляет десятичный логарифм (по основанию 10) Decimal числа
print()

num1 = Decimal('-1.4568769017')
num2 = Decimal('0.523')
"""
sign – знак числа (0 для положительного числа и 1 для отрицательного числа);
digits – цифры числа;
exponent – значение экспоненты (количество цифр после точки, умноженное на −1).
"""
print(num1.as_tuple()) # DecimalTuple(sign=1, digits=(1, 4, 5, 6, 8, 7, 6, 9, 0, 1, 7), exponent=-10)
print(num2.as_tuple()) # DecimalTuple(sign=0, digits=(5, 2, 3), exponent=-3)
print()

num = Decimal('-1.4568769017')
num_tuple = num.as_tuple()

print(num_tuple.sign) # 1
print(num_tuple.digits) # (1, 4, 5, 6, 8, 7, 6, 9, 0, 1, 7)
print(num_tuple.exponent) # -10
print()

print(getcontext()) # Context(prec=28, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999, capitals=1, clamp=0,
# flags=[Inexact, FloatOperation, Rounded], traps=[InvalidOperation, DivisionByZero, Overflow])
# точность 28 знаков, округление к ближайшему четному, пределы по экспоненте ± 999999
# capitals – это про заглавную Е при печати, включенные ловушки – неправильная операция, деление на ноль, переполнение.
print()

getcontext().prec = 3      # устанавливаем точность в 3 знака

num = Decimal('3.1415')

print(num) # 3.1415
print(num * 1) # 3.14
print(num * 2) # 6.28
print(num / 2) # 1.57
print()

getcontext().prec = 4                    # устанавливаем точность числа

num = Decimal('3.1415926535')

# print(num.quantize(Decimal('1.0000')))    #  decimal.InvalidOperation: [<class 'decimal.InvalidOperation'>]
print(num.quantize(Decimal('1.000')))    #  3.142 округление до 3 цифр в дробной части
print(num.quantize(Decimal('1.00')))     #  3.14 округление до 2 цифр в дробной части
print(num.quantize(Decimal('1.0')))      #  3.1 округление до 1 цифр в дробной части
print()

num = Decimal('3.476')

print(num.quantize(Decimal('1.00'), ROUND_CEILING)) # 3.48 округление в направлении бесконечности (Infinity)
print(num.quantize(Decimal('1.00'), ROUND_FLOOR)) # 3.47 округляет в направлении минус бесконечности (- Infinity)
print(num.quantize(Decimal('1.00'), ROUND_DOWN)) # 3.47 округление в направлении нуля
print(num.quantize(Decimal('1.00'), ROUND_HALF_EVEN)) # 3.48 округление до ближайшего четного числа, число 6.5
# округлится не до 7, а до 6
print(num.quantize(Decimal('1.00'), ROUND_HALF_DOWN)) # 3.48 округление до ближайшего нуля
print(num.quantize(Decimal('1.00'), ROUND_UP)) # 3.48 округление от нуля
print(num.quantize(Decimal('1.00'), ROUND_05UP)) # 3.47 округление от нуля (если последняя цифра после округления до
# нуля была бы 0 или 5, в противном случае – к нулю)
print()
num = Decimal('0.1')
if num*3 == Decimal('0.3'):
    print('YES') # YES
else:
    print('NO')
print()

s = '1.34 3.45 1.00 0.03 9.25'

numbers = [Decimal(i) for i in s.split()]

maximum = max(numbers)
minimum = min(numbers)

numbers.sort()

print(maximum) # 9.25
print(minimum) # 0.03
print(numbers) # [Decimal('0.03'), Decimal('1.00'), Decimal('1.34'), Decimal('3.45'), Decimal('9.25')]
print()
from decimal import Decimal as D

num1 = D('1.5') + D('3.2')
num2 = D('1.4') * D('2.58')

print(num1)
print(num2)