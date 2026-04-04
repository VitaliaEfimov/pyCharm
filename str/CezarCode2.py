def get_chr(ind, islower, a, m):
    # Нормализуем индекс, чтобы он был в пределах [0, m]
    ind = ind % (m + 1)  # Берем остаток от деления на длину алфавита

    if islower:
        return a[ind]
    else:
        return a[ind].upper()


def print_var(a, s):
    for k in range(-len(a), 0):  # Исправлено: диапазон до 0, так как -1 уже включительно
        r = ''
        for i in s:
            if i.isalpha():
                islower = i == i.lower()
                ind = a.find(i.lower()) + k
                r += get_chr(ind, islower, a, len(a) - 1)
            else:
                r += i
        print(k, r)


# a = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
a = 'abcdefghijklmnopqrstuvwxyz'
s = input()
print_var(a, s)
