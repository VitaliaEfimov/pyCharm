from fractions import Fraction as F

numbers = ['3.1415', '-2.8', '4.123', '7.856']
for i in numbers:
    print(f'{i} = {F(i)}')
"""
3.1415 = 6283/2000
-2.8 = -14/5
4.123 = 4123/1000
7.856 = 982/125
"""
print()

s = '0.21 74.5 12.3 -11.77 48.6542 114.55'
l = [F(i) for i in s.split()]
print(min(l) + max(l)) # 5139/50
print()

n = int(4)
m = int(6)
print(F(n, m))
print()

s1 = '1/2'
s2 = '1/3'
f1 = F(s1)
f2 = F(s2)
print(f'{s1} + {s2} = {f1 + f2}') # 1/2 + 1/3 = 5/6
print(f'{s1} - {s2} = {f1 - f2}') # 1/2 - 1/3 = 1/6
print(f'{s1} * {s2} = {f1 * f2}') # 1/2 * 1/3 = 1/6
print(f'{s1} / {s2} = {f1 / f2}') # 1/2 / 1/3 = 3/2
print()

def sumf(j):
    su = F(0)
    for k in range(1, j+1):
        su += F(1, k**2)
    return su
g = int(6)
print(sumf(g)) # 5369/3600
print()

from math import *

n = 6
s = F(0)
for i in range(n):
    s += F(1, factorial(i+1))
print(s) # 1237/720
print()

n = int(10)
r = F(0)
for i in range(1, n):
    if gcd(i, n - i) == 1 and i < n - i:
        r = F(i, n - i)

print(r) # 3/7
print()

n = int(5)
l = []
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if gcd(j, i) == 1 and F(j, i) < 1:
            l.append(F(j, i))
print(*sorted(l), sep = '\n')
"""
1/5
1/4
1/3
2/5
1/2
3/5
2/3
3/4
4/5
"""
