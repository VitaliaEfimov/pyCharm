n = int(input())
b =  ''

print(f'{n:b}')
print(hex(n))
print(oct(n))
print(bin(n))

print(bin(n)[2:])

s = format(n, 'b')
print(s)

while n > 0:
    b += str(n % 2)
    n //= 2

print(b[::-1])