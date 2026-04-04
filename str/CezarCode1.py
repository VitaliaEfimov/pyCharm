def get_chr(ind, islower, a, m):
    if ind > m:
        if islower:
            return a[ind - m]
        else:
            return a[ind - m].upper()
    else:
        if islower:
            return a[ind]
        else:
            return a[ind].upper()
# a = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
a = 'abcdefghijklmnopqrstuvwxyz'
s = input()
r = ''
rot = int(input())
for i in s:
    if i.isalpha():
        islower = i == i.lower()
        ind = a.find(i.lower()) + rot
        r += get_chr(ind, islower, a, len(a) - 1)
    else:
        r += i
print(r)