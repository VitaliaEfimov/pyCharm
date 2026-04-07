def is_even(num): # Предикат
    return num % 2 == 0

print(True == 1) # True
print(False == 0) # True
print(bool('Beegeek')) # True
print(bool(17)) # True
print(bool(-17)) # True
print(bool(['apple', 'cherry'])) # True
print(bool()) # False
print(bool('')) # False
print(bool(0)) # False
print(bool([])) # False
print(is_even(6)) # True
print(isinstance(3, int)) # True
print(isinstance(3.5, float)) # True
print(isinstance('Beegeek', str)) # True
print(isinstance([1, 2, 3], list)) # True
print(isinstance(True, bool)) # True
print(type(3)) # <class 'int'>
print(type(3.5)) # <class 'float'>
print(type('Beegeek')) # <class 'str'>
print(type([1, 2, 3])) # <class 'list'>
print(type(True)) # <class 'bool'>