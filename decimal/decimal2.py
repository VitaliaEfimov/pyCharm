from decimal import *


s = '0.0 5.42 8.63 10.25 1.6 -8.5 -13.0'
l = [Decimal(i) for i in s.split()]
print(min(l) + max(l)) # -2.75
print()

s = '12.3 1.8 3.6 -1.2 0.5 -14.2 86.5 10.3'
l = [Decimal(i) for i in s.split()]
print(sum(l)) # 99.6
print(*sorted(l)[-5:][::-1]) # 86.5 12.3 10.3 3.6 1.8
print(*sorted(l, reverse=True)[:5]) # 86.5 12.3 10.3 3.6 1.8
print()

d = Decimal('0.1244354689')
t = d.as_tuple().digits
e = d.as_tuple().exponent
minimum = min(t)
if len(t) <= -1*(e):
    minimum = 0
print(minimum + max(t)) # 9
print()

d = Decimal('1.1')
print(d.exp() + d.ln() + d.log10() + d.sqrt()) # 4.189677737079134559844013562