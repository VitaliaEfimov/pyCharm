n = int(input())
k = int(input())
l = [True] * n  # True - жив, False - убит
index = 0  # текущая позиция
remaining = n  # сколько осталось живых

while remaining > 1:
    # Считаем k живых людей
    count = 0
    while count < k:
        if l[index]:  # если человек жив
            count += 1
        if count < k:  # если ещё не дошли до k
            index = (index + 1) % n

    # Убиваем текущего
    l[index] = False
    remaining -= 1

    # Переходим к следующему живому
    while not l[index]:
        index = (index + 1) % n

# Находим индекс выжившего (прибавляем 1 для номера человека)
print(l.index(True) + 1)