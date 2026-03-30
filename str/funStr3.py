print('.isalnum() Получаем состоит ли исходная строка из буквенно-цифровых (ИЛИ) символов. Пробел не является таковым, если он есть в строке - False')
print("'abc123'", 'abc123'.isalnum()) # True
print("'abc$*123'", 'abc$*123'.isalnum()) # False
print("''", ''.isalnum()) # False
print("'cyberpunk 2077'", 'cyberpunk 2077'.isalnum()) # False

print('.isalpha() Проверяем состоит ли исходная строка только из буквенных символов.')
print("'ABCabc'", 'ABCabc'.isalpha()) # True
print("abc123", 'abc123'.isalpha()) # False
print("''", ''.isalpha()) # False

print('.isdigit() Проверяем, что строка состоит только из цифр - что это число')
print("1234567", '1234567'.isdigit()) # True
print("abc123", 'abc123'.isdigit()) # False
print("''", ''.isdigit()) # False

print('.islower() Проверяем, что в строке буквы в нижнем регистре, игнорируя все небуквенные символы. Если букв нет вообще - False')
print("'abc'", 'abc'.islower()) # True
print("'abc1$d'", 'abc1$d'.islower()) # True
print("'Abc1$D'", 'Abc1$D'.islower()) # False
print("'12234'", '12234'.islower()) # False

print('.isupper() Проверяем, что в строке буквы в верхнем регистре, игнорируя все небуквенные символы. Если букв нет вообще - False')
print("'ABC'", 'ABC'.isupper()) # True
print("'ABC1$D'", 'ABC1$D'.isupper()) # True
print("'Abc1$D'", 'Abc1$D'.isupper()) # False
print("'5678'", '5678'.isupper()) # False
print("'!?_&'", '!?_&'.isupper()) # False

print('.isspace() Определяет, состоит ли исходная строка только из пробельных символов. Если строка пустая - False')
print("'      '", '      '.isspace()) # True
print("' sadhaskjd '", ' sadhaskjd '.isspace()) # False
print("''", ''.isspace()) # False