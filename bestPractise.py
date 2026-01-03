# a, b, c = (int(input()) for _ in '123')
# print(a, b, c)

import os
import httplib2
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build

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

print(sum(int(x) for x in map(input, [''] * 3) if int(x) > 0))

list1 = [1, 2, 3, 4]
list2 = [4, 5, 6, 7]

result = map(lambda x, y: x + y, list1, list2)
print(result)
print(list(result))  # [5, 7, 9]

