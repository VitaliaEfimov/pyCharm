# a, b, c = (int(input()) for _ in '123')
# print(a, b, c)

import os
import httplib2
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build
import re

def get_service_sacc():
    creds_json = os.path.dirname(__file__) + "/creds/sacc1.json"
    scopes = ['https://www.googleapis.com/auth/spreadsheets']

    creds_service = ServiceAccountCredentials.from_json_keyfile_name(creds_json, scopes).authorize(httplib2.Http())
    return build('sheets', 'v4', http=creds_service)

id = 'dfslkjfad'

resp = get_service_sacc().spreadsheets().values().batchGet(spreadsheetId=id, ranges=["Популярное", "Лист3"]).execute()

simvol = input()
n = int(input())

for i in range(1, n + 1):
    # Печатаем пробелы перед символами (для центрирования)
    print(" " * (n - i), end="")
    # Печатаем символы (2i - 1, чтобы получить нечётное количество)
    print(simvol * (2 * i - 1))

m = list(map(int, iter(input, "0")))
print(max(filter(lambda x: x % 11 == 0, m)))

m = list(map(str, iter(input, "exit")))
print(''.join(filter(lambda s: 's' in s, m)))

x = [float(input()) for x in range(4)]

print(max(int(i) for i in iter(input, '0') if int(i) % 11 == 0))

nums = [int(i) for i in iter(input, '0') if int(i) % 5 != 0 or int(i) % 10 == 6]
if nums:
    average = sum(nums) / len(nums)
    print(average)
else:
    print("таких цифр нет")

print([*map(int,input().split())][::-1])

print(('Не п', 'П')[-1 < int(input()) < 17] + 'ринадлежит')

flag = False
print(('NO', 'YES')[flag])
print(int(flag))

print(sum(int(x) for x in map(input, [''] * 3) if int(x) > 0))

list1 = [1, 2, 3, 4]
list2 = [4, 5, 6, 7]

result = map(lambda x, y: x + y, list1, list2)
print(result)
print(list(result))  # [5, 7, 9, 11]

counter = 0

while (name := input()) != "Левон":
    counter += 1
    if name == "Александра":
        first_index = counter

l = list(map(str.strip, open(0)))
print(l.index('Левон') - l.index('Александра') - 1)

s = input()
lst = list(map(int, s))

h = 1
m = 1
print(f'{h:02d}:{m:02d}')

# Вывод каждого элемента с новой строки
[print(f'{i}) {ch}') for i,ch in enumerate(input(),1)]
[print('{}) {}'.format(*z)) for z in enumerate(input(), 1)]
print(*[f'{i+1}) {lst[i]}' for i in range(len(input()))], sep='\n')
print(*([f"{index + 1}) {char}" for index, char in enumerate(input())]), sep = '\n')

# проверка, что в строке есть цифры
print(['Цифр нет','Цифра'][any(map(str.isdigit,input()))])
print(('Цифр нет', 'Цифра')[bool(re.search(r'\d', input()))])

# количество символов
s = input()
print(f'''Символ + встречается {s.count('+')} раз
Символ * встречается {s.count('*')} раз''')
print(f'Символ + встречается {len(list(i for i in s if i == "+"))} раз')
print(f'Символ * встречается {len(list(i for i in s if i == "*"))} раз')

flag = False
print('YES' if flag else 'NO')

print(sum(input().count('11') >= 3 for _ in range(int(input()))))
# Использование регулярного выражения для проверки валидности номера машины
print('YES' if re.search("^[АВЕКМНОРСТУХ][0-9]{3}[АВЕКМНОРСТУХ]{2}_[0-9]{2,3}$", input()) else 'NO')
s = 'А123ВС_45'
alf = 'АВЕКМНОРСТУХ'
all(x in alf for x in [s[i] for i in [0,4,5]])