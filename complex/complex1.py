z1 = 5 + 7j
z2 = 1j
z3 = -3 + 5J
z4 = 1.5 + 3.2j

print(z1, z2, z3, z4, sep='\n')
print(type(z1))
print()

"""
(5+7j)
1j
(-3+5j)
(1.5+3.2j)
<class 'complex'>
"""

z1 = -3 + 2j              # создание на основе литерала
z2 = complex(6, -8)       # z2 = 6 - 8j
z3 = complex(0, 2.5)      # z3 = 2.5j
z4 = complex(5, 0)        # z4 = 5 + 0j
z5 = complex('3+4j')      # создание на основе строки

print(z1, z2, z3, z4, z5, sep='\n')
print()
"""
(-3+2j)
(6-8j)
2.5j
(5+0j)
(3+4j)
"""

z1 = 1 + 3j
z2 = -3 + 2j

print('z1 + z2 =', z1 + z2)
print('z1 - z2 =', z1 - z2)
print('z1 * z2 =', z1 * z2)
print('z1 / z2 =', z1 / z2)
print('z1^20 =', z1**20)
print()
"""
z1 + z2 = (-2+5j)
z1 - z2 = (4+1j)
z1 * z2 = (-9-7j)
z1 / z2 = (0.23076923076923078-0.8461538461538461j)
z1^20 = (9884965888-1512431616j)
"""

z = 1 + 3j

print(z + 5)
print(z - 2)
print(3*z)
print(z/2)
print()
"""
(6+3j)
(-1+3j)
(3+9j)
(0.5+1.5j)
"""

z = 3+4j

print('Действительная часть =', z.real) # Действительная часть = 3.0
print('Мнимая часть =', z.imag) # Мнимая часть = 4.0
print()

z = 3+4j

print('Сопряженное число =', z.conjugate()) # Сопряженное число = (3-4j)
print()

z = 3+4j

print('Модуль числа =', abs(z)) # Модуль числа = 5.0
print()

import cmath

z = 2+3j
print(cmath.phase(z)) # полярный угол 0.982793723247329
print(cmath.polar(z)) # полярные координаты (3.605551275463989, 0.982793723247329)