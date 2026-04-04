from random import *
# Угадайка
def is_valid(num):
    if num.isdigit() and 1 <= int(num) <= 100:
        return True
    else:
        return False

print('Добро пожаловать в игру "Угадайка"')
d = randint(1, 100)
c = 0
while True:
    n = input('Введите число от 1 до 100 ')
    c += 1
    if not is_valid(n):
        print('Вы ввели не валидное значение. Введите число от 1 до 100')
    if int(n) < d:
        print('Введенное число меньше загаданного')
    elif d == int(n):
        print(f'Вы угадали, количество попыток: {c}')
        break
    else:
        print('Введенное число больше загаданного')
