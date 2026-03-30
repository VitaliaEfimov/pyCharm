print('a' > 'b') # False Сравниваем по ord(chr)
print('a' < 'z') # True
print('d' > 'D') # True
print('Ы' < 'ы') # True
print('hello' > 'hell') # True
print('men' < 'mya') # True При первом не совпадении символов сравниваем по ord(chr)
# print('45' > 44) # TypeError: '>' not supported between instances of 'str' and 'int'
print(max('tree', 'try', 'true')) # try
print(min('cat', 'car', 'cape')) # cape
print(sorted(['a', 'an', 'aunt', 'An'])) # ['An', 'a', 'an', 'aunt']
print(sorted(['0', '10', '11', '010', '100'])) # ['0', '010', '10', '100', '11']
print(sorted(['a10', 'a', 'a11', 'a9'])) # ['a', 'a10', 'a11', 'a9']
print(sorted(['9', '10', '11'])) # ['10', '11', '9']
print(max(9, 10, 11)) # 11
print(max('9', '10', '11')) # 9
print(min('9', '10', '11') + max('9', '10', '11')) # 109