numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(len(numbers)):
    print(numbers[i]) # Вывод всех символов через индекс
for num in numbers:
    print(num) # Вывод через итератор
for num in numbers:
    print(num, end=' ') # Вывод элементов через пробел на одной строке
print()
print(*numbers) # Распаковка. Вывод элементов через пробел на одной строке
print()
print(*numbers, sep = '\n') # Распаковка. Вывод элементов на новой строке
s = 'Python'
print(*s)
print()
print(*s, sep='\n')

n = int(input())
lst = []

for i in range(n):
    lst.append(int(input()))
minn = min(lst)
maxx = max(lst)
el = 0
for i in range(n):
    if lst[el] == maxx or lst[el] == minn:
        del lst[el] # Удаляем максимум и минимум
    else:
        el +=1
print(*lst, sep ='\n')