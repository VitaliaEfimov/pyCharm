
from random import *

seed(1)   # явно устанавливаем начальное значение для генератора случайных чисел. Меняется после вызовов из random

for _ in range(10):
    print(randint(1, 100))

num1 = randint(0, 17)
num2 = randint(-5, 5)

print()
print(num1)
print(num2)

num = randrange(0, 101, 10)
print()
print(num)

num = uniform(1.5, 17.3)
print()
print(num)

num = random()
print()
print(num)

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
shuffle(numbers)
print(numbers)

print(choice('BEEGEEK'))
print(choice([1, 2, 3, 4]))
print(choice(['a', 'b', 'c', 'd']))

print(sample(numbers, 1))
print(sample(numbers, 2))
print(sample(numbers, 3))
print(sample(numbers, 5))
# print(sample(numbers, 10)) # ValueError: Sample larger than population or is negative