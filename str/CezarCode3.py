def get_chr(ind, islower, a, m):
    # Нормализуем индекс, чтобы он был в пределах [0, m]
    ind = ind % m  # Берем остаток от деления на длину алфавита

    if islower:
        return a[ind]
    else:
        return a[ind].upper()
# a = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
a = 'abcdefghijklmnopqrstuvwxyz'
s = input()
r = ''
rot = 0
w = ''
for i in s:
    if i.isalpha():
        w += i
    else:
        for c in w:
            islower = c == c.lower()
            ind = a.find(c.lower()) + len(w)
            r += get_chr(ind, islower, a, len(a))
        w = ''
        r += i
if len(w) != 0:
    for c in w:
        islower = c == c.lower()
        ind = a.find(c.lower()) + len(w)
        r += get_chr(ind, islower, a, len(a))
print(r)