var = None
print(type(var)) # <class 'NoneType'>
if var is None:  # используем оператор is
    print('None')
else:
    print('Not None')
print(None == 17) # False
print(None == 3.14) # False
print(None == True) # False
print(None == [1, 2, 3]) # False
print(None == 'Beegeek') # False
# print(None > 0) # TypeError: '>' not supported between instances of 'NoneType' and 'int'