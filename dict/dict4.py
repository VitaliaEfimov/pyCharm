words = {}

a, b = 'word1 word2'.split()
words[a], words[b] = b, a
print(words) # {'word1': 'word2', 'word2': 'word1'}

def se(word):
    res = {}
    for i in word.lower():
        res[i] = res.get(i, 0) + 1
    return res

s = '*!*!*?'
d1 = se(s)
d2 = {3: 'а',
2: 'н',
1 : 'с'}
r =''
for c in s:
    r += d2[d1[c]]
print(r)

l = 'a b c a a d c'.split()
d = {}
r = []
for c in l:
    if d.get(c) is None:
        r.append(c)
        d[c] = 1
    else:
        r.append(c + '_' +str(d[c]))
        d[c] += 1
print(*r) # a b c a_1 a_2 d c_1

def discountable(lst):
    res = {}
    for e in lst:
        res[e] = res.get(e, 0) + 1
    return res

text = ('London is the capital of Great Britain. More than six million people live in London. London lies on both banks '
        'of the river Thames. It is the largest city in Europe and one of the largest cities in the world. London is not '
        'only the capital of the country, it is also a very big port, one of the greatest commercial centres in the world, '
        'a university city, and the seat of the government of Great Britain!').lower()
for char in ',.!?;:':
    text = text.replace(char, ' ')
ws = text.split()
d = discountable(ws)
minimum = min(d.values())
r = [i for i in d if d[i] == minimum]
print(sorted(r)[0]) # also

from datetime import datetime, timedelta
d1 = {}
time_format = "%H:%M"
time1 = ['198351: 14:20', '976244: 14:22' , '763482: 14:22', '974311: 14:26', '187646: 14:29']
for i in time1:
    ID, time = i.split(': ')
    d1[ID] = datetime.strptime(time, time_format)
time2 = ['976244: 14:59', '974311: 15:03', '198351: 16:51']
for i in time2:
    ID, time = i.split(': ')
    t = datetime.strptime(time, time_format)
    if t < d1[ID]:
        t += timedelta(days=1)
    dt = (t - d1[ID]).total_seconds()
    if dt > 7200:
        print(f'{ID}: {int((dt - 7200) / 60 * 3)}₽')
    else:
        print(f'{ID}: плата не взимается')
"""
976244: плата не взимается
974311: плата не взимается
198351: 93₽
"""