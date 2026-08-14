recipients = {
    'Humanities': 409,
    'Biology': 1473,
    'Engineering': 1343,
    'Physical Sciences': 1131,
    'Medicine': 153,
}

recipients.update([('Scripps', 131), ('Math', 3456)]) # {'Humanities': 409, 'Biology': 1473, 'Engineering': 1343, 'Physical Sciences': 1131, 'Medicine': 153, 'Scripps': 131, 'Math': 3456}
print(recipients)
recipients = {
    'Humanities': 409,
    'Biology': 1473,
    'Engineering': 1343,
    'Physical Sciences': 1131,
    'Medicine': 153,
}

recipients.update({'Scripps': 131, 'Math': 3456}) # {'Humanities': 409, 'Biology': 1473, 'Engineering': 1343, 'Physical Sciences': 1131, 'Medicine': 153, 'Scripps': 131, 'Math': 3456}
print(recipients)

emails = {
    'gmail.com': ['johnny', 'monkey-man'],
    'hotmail.com': ['chani'],
    'yandex.ru': ['petrpn', 'rtgxv5dsfsd4'],
}

l = []
for i in emails:
    for j in emails[i]:
        l.append(j + '@' + i)
print(*sorted(l), sep='\n')
"""
chani@hotmail.com
johnny@gmail.com
monkey-man@gmail.com
petrpn@yandex.ru
rtgxv5dsfsd4@yandex.ru
"""
dna = {'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A'}
print(*[dna[c] for c in 'ACTG'], sep='') # UGAC

l = 'прием Хьюстон Хьюстон как слышно прием меня слышно прием хьюстон'.split()
d = {}
for i in l:
    d[i] = d.setdefault(i, 0) + 1
    print(d[i], end=' ') # 1 1 2 1 1 2 1 2 3 1
print()

d = {
    1: "AEILNORSTU",
    2: "DG",
    3: "BCMP",
    4: "FHVWY",
    5: "K",
    8: "JX",
    10: "QZ"
}
w = 'FRESHENER'
s = 0
for i in w:
    for k in d:
        if i in d[k]:
            s += k
print(s) # 15

def build_query_string(params):
    # res = [f'{k}={v}' for k, v in params.items()]
    # return '&'.join(sorted(res))
    l=[]
    for k,v in params.items():
        l.append(str(k) + '=' + str(v))
    return '&'.join(sorted(l))

print(build_query_string({'name': 'timur', 'age': 28})) # age=28&name=timur

def merge(l):
    d = {}
    for i in l:
        for j in i:
            d.setdefault(j, set())
            d[j].add(i[j])
    return d

print(
    merge(
        [
            {'d': 2, 'x': 4},
            {'x': 1, 'r': -2},
            {'d': 2},
            {'r': 2},
        ]
    )
) # {'d': {2}, 'x': {1, 4}, 'r': {2, -2}}
cs1 = ["my_pycode.exe W X", "log_n X W R", "ave R", "lucky_m W R", "dnsss.py W"]
cs2 = ["execute ave", "read dnsss.py", "write log_n", "execute log_n", "read ave", "write my_pycode.exe"]

f = {}
for i in range(len(cs1)):
    l =[j for j in cs1[i].split()]
    f[l[0]] = l[1:]
s = {'write': 'W', 'read': 'R','execute': 'X'}
for i in range(len(cs2)):
    l =[j for j in cs2[i].split()]
    if s[l[0]] in f[l[1]]:
        print('OK')
    else:
        print('Access denied')
"""
Access denied
Access denied
OK
OK
OK
OK
"""

s = ["Руслан Пирог 1", "Тимур Карандаш 5", "Руслан Линейка 2", "Тимур Тетрадь 12", "Руслан Хлеб 3"]

d = {}
for i in range(len(s)):
    name, item, c = s[i].split()
    count = int(c)
    dn = d.setdefault(name, {})
    dn[item] = dn.get(item, 0) + count
for i in sorted(d):
    print(i + ':')
    for j in sorted(d[i]):
        print(j, d[i][j])

"""
Руслан:
Линейка 2
Пирог 1
Хлеб 3
Тимур:
Карандаш 5
Тетрадь 12
"""
