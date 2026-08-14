""" Словари могут содержать другие словари, которые сами, в свою очередь, содержат словари, и так далее на любую глубину.
 Такие словари называются вложенными словарями.

✅ Вложенный словарь создается как обычный, только каждое значение в нем – другой словарь.

✅ Для того чтобы получить значения определенных элементов во вложенном словаре, необходимо указать их ключи
в нескольких квадратных скобках.

✅ Общий вид генератора словаря следующий:

{ключ: значение for переменная in последовательность if условие},


где переменная — имя некоторой переменной, последовательность — последовательность значений, которые она принимает
(любой итерируемый объект), ключ: значение — некоторое выражение, как правило, зависящее от использованной в генераторе
словаря переменной, которой будут заполнены элементы словаря, условие (необязательное) – в словарь попадут элементы,
для которых условие истинно.
"""

info = {'emp1': {'name': 'Timur', 'job': 'Teacher'},
        'emp2': {'name': 'Ruslan', 'job': 'Developer'},
        'emp3': {'name': 'Rustam', 'job': 'Tester'}}

info['emp1']['job'] = 'Manager'

print(info['emp1']) # {'name': 'Timur', 'job': 'Manager'}
print(info) # {'emp1': {'name': 'Timur', 'job': 'Manager'}, 'emp2': {'name': 'Ruslan', 'job': 'Developer'}, 'emp3': {'name': 'Rustam', 'job': 'Tester'}}

info = {'emp1': {'name': 'Timur', 'job': 'Teacher'},
        'emp2': {'name': 'Ruslan', 'job': 'Developer'},
        'emp3': {'name': 'Rustam', 'job': 'Tester'}}

for emp in info:
    print('Employee ID:', emp)
    for key in info[emp]:
        print(key + ':', info[emp][key])
    print()

"""
Employee ID: emp1
name: Timur
job: Teacher

Employee ID: emp2
name: Ruslan
job: Developer

Employee ID: emp3
name: Rustam
job: Tester
"""

squares = {i: i**2 for i in range(6)} # Генератор словаря
print(squares) # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

dct = {c: c * 3 for c in 'ORANGE'}

print(dct) # {'O': 'OOO', 'R': 'RRR', 'A': 'AAA', 'N': 'NNN', 'G': 'GGG', 'E': 'EEE'}

lst = ['ReD', 'GrEeN', 'BlUe']
dct = {c.lower(): c.upper() for c in lst} # Использование методов

print(dct) # {'red': 'RED', 'green': 'GREEN', 'blue': 'BLUE'}

dict1 = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F'}
selected_keys = [0, 2, 5]

dict2 = {k: dict1[k] for k in selected_keys} # Отбор по необходимым ключам

print(dict2) # {0: 'A', 2: 'C', 5: 'F'}

squares = {i: i**2 for i in range(10) if i % 2 == 0} # Добавляем условие

print(squares) # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

squares = {i: {j: j**2 for j in range(i + 1)} for i in range(5)} # Вложенный словарь

for value in squares.values():
    print(value)
"""
{0: 0}
{0: 0, 1: 1}
{0: 0, 1: 1, 2: 4}
{0: 0, 1: 1, 2: 4, 3: 9}
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
"""

months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}

result = {months[i]: i for i in months}
print(result) # {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}

numbers = [-3, 6, 4, 76, 2, -1, 2]

print({i: numbers[i]**2 for i in range(len(numbers))}) # {0: 9, 1: 36, 2: 16, 3: 5776, 4: 4, 5: 1, 6: 4}

colors = {'a1': 'Blue', 'b2': 'Orange', 'b4': None, 'a6': 'Red', 'c4': None}
print({k: v for k, v in colors.items() if v}) # {'a1': 'Blue', 'b2': 'Orange', 'a6': 'Red'}

favorite_numbers = {
    'scarlett': 41, 'den': 22, 'viktor': 321, 'lera': 777, 'mahad': 4,
    'manny': 4, 'ken': 8423, 'borya': 12
}

print({k: v for k, v in favorite_numbers.items() if len(str(v)) == 2}) # {'scarlett': 41, 'den': 22, 'borya': 12}

s = '3:animal 4:house 8:tree 2:color 21:moon 31:fire 12:ship'

print({int(i.split(':')[0]): i.split(':')[1] for i in s.split()}) # {3: 'animal', 4: 'house', 8: 'tree', 2: 'color', 21: 'moon', 31: 'fire', 12: 'ship'}

numbers = [24, 5, 17, 9, 28, 84, 62]

print({i: [j for j in range(1, i+1) if i%j==0] for i in numbers}) # {24: [1, 2, 3, 4, 6, 8, 12, 24], 5: [1, 5], 17: [1, 17], 9: [1, 3, 9], 28: [1, 2, 4, 7, 14, 28], 84: [1, 2, 3, 4, 6, 7, 12, 14, 21, 28, 42, 84], 62: [1, 2, 31, 62]}

words = ['кошка', 'собака', 'мышь']

print({s: [ord(c) for c in s] for s in words}) # {'кошка': [1082, 1086, 1096, 1082, 1072], 'собака': [1089, 1086, 1073, 1072, 1082, 1072], 'мышь': [1084, 1099, 1096, 1100]}

letters = {4: 'К', 65: 'Щ', 12: 'П', 41: 'М', 36: 'У'}
remove_keys = [12, 65, 14, 37]

print({k: v for k, v in letters.items() if k not in remove_keys}) # {4: 'К', 41: 'М', 36: 'У'}

students = {'Сергей': (165, 62), 'Дима': (178, 61), 'Катя': (162, 62), 'Диана': (168, 69)}

print({k: v for k,v in students.items() if v[0]>  167 and v[1] < 75}) # {'Дима': (178, 61), 'Диана': (168, 69)}

tuples = [
    (1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12), (13, 14, 15), (16, 17, 18),
    (19, 20, 21), (22, 23, 24), (25, 26, 27), (28, 29, 30), (31, 32, 33), (34, 35, 36),
]

print({t[0]: t[1:3] for t in tuples}) # {1: (2, 3), 4: (5, 6), 7: (8, 9), 10: (11, 12), 13: (14, 15), 16: (17, 18), 19: (20, 21), 22: (23, 24), 25: (26, 27), 28: (29, 30), 31: (32, 33), 34: (35, 36)}

ids = ['emp1', 'emp2', 'emp3']
emp_info = [{'name': 'Timur', 'job': 'Teacher'},
            {'name': 'Ruslan', 'job': 'Developer'},
            {'name': 'Rustam', 'job': 'Tester'}]

info = dict(zip(ids, emp_info))
print(info) # {'emp1': {'name': 'Timur', 'job': 'Teacher'}, 'emp2': {'name': 'Ruslan', 'job': 'Developer'}, 'emp3': {'name': 'Rustam', 'job': 'Tester'}}

student_ids = ['X142', 'B065', 'X144']
student_names = ['Nikita Karpov', 'Anna Chernova', 'Ruslan Magarov']
student_grades = [88, 85, 62]

print([{student_ids[i]: {student_names[i]:student_grades[i]}} for i in range(len(student_ids))]) # [{'X142': {'Nikita Karpov': 88}}, {'B065': {'Anna Chernova': 85}}, {'X144': {'Ruslan Magarov': 62}}]
