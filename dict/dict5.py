
homoglyphs = {
    'e': 'е', 'y': 'у', 'o': 'о', 'p': 'р', 'a': 'а',
    'ʍ': 'м', 'ʙ': 'в', 'Φ': 'Ф', 'k': 'к', 'x': 'х',
    'c': 'с', 'E': 'Е', 'T': 'Т', 'ȹ': 'ф', 'Ͷ': 'И',
    'ʜ': 'н', 'O': 'О', 'P': 'Р', 'A': 'А', 'H': 'Н',
    'K': 'К', 'Ƅ': 'ь', 'ͷ': 'и', 'ɯ': 'ш', 'X': 'Х',
    'C': 'С', 'B': 'В', 'M': 'М', 'π': 'п', '3': 'З',
    'Γ': 'Г', 'ʮ': 'ч',
}


def replace_homoglyphs(text):
    new_text = ''
    for c in text:
        new_text += homoglyphs.get(c, c)

    return new_text

text = 'XoʮeɯƄ зapaбaтыʙaтƄ oт 5K ʙ cyтkͷ? Haπͷɯͷ ʜaʍ ʙ ʮaтe.'
print(replace_homoglyphs(text)) # Хочешь зарабатывать от 5К в сутки? Напиши нам в чате.

def transform(s):
    res = {}
    for i in range(len(s)):
        res.setdefault(s[i], set()).add(i)

    return res

print(transform('Аметист')) # {'А': {0}, 'м': {1}, 'е': {2}, 'т': {3, 6}, 'и': {4}, 'с': {5}}

black_list = [
    '45.34.12.200', '78.91.204.34',
    '78.94.127.35', '96.124.37.82',
]
white_list = [
    '14.231.64.173', '75.34.2.179',
]
ip_access_lists = {
    'black list': black_list,
    'white list': white_list,
}

def is_access_allowed(ip, mode, ip_access_lists):
    r = None
    if mode == 1:
        r = ['НЕТ', 'ДА'][ip not in ip_access_lists['black list']]
    else:
        r = ['НЕТ', 'ДА'][ip in ip_access_lists['white list']]
    return r

print(
    is_access_allowed(
        '224.27.189.35',
        1,
        ip_access_lists,
    )
) # ДА

def dict_diff(data1, data2):
    diff = {}
    k = set(data1.keys()) | set(data2.keys())
    for i in k:
        if data1.get(i) and not data2.get(i):
            diff[i] = 'deleted'
        elif not data1.get(i) and data2.get(i):
            diff[i] = 'added'
        elif data1.get(i) and data2.get(i):
            if data1.get(i) == data2.get(i):
                diff[i] = 'unchanged'
            else:
                diff[i] = 'changed'
    return diff

data1 = {'one': 1, 'two': 2, 'four': 4}
data2 = {'two': 2.5, 'three': 3, 'four': 4}

print(dict_diff(data1, data2)) # {'two': 'changed', 'four': 'unchanged', 'three': 'added', 'one': 'deleted'}

def add_query_string(d, p):
    s = d + '?'
    for i in p:
        s += i + '=' + str(p[i]) + '&'
    return s[:-1]

print(add_query_string('pygen.ru', {'per': '10', 'page': 1})) # pygen.ru?per=10&page=1

p = {
    'яблоко': '🍎', 'хлеб': '🍞', 'конфеты': '🍬', 'лимон': '🍋',
    'морковь': '🥕', 'огурец': '🥒', 'помидор': '🍅', 'яйцо': '🥚',
    'чеснок': '🧄', 'авокадо': '🥑', 'спички': '🥢', 'соль': '🧂',
    'филе говядины': '🥩', 'киви': '🥝', 'лук': '🧅', 'сыр': '🧀',
}

def print_product_list(l):
    d = {}
    for i in l:
        d[p.get(i, i)] = l.count(i)
    for i in d:
        print(i + ': ' + str(d[i]))

product_list = [
    'молоко', 'яйцо', 'колбаса', 'лук',
    'помидор', 'помидор', 'майонез',
    'хлеб', 'лук', 'сливочное масло',
]
print_product_list(product_list)
"""
молоко: 1
🥚: 1
колбаса: 1
🧅: 2
🍅: 2
майонез: 1
🍞: 1
сливочное масло: 1
"""

def getdictcount(s):
    d = {}
    for i in s:
        d[i] = d.setdefault(i, 0) + 1

    return d
def scrabble(letters, word):
    d1 = getdictcount(letters.lower())
    d2 = getdictcount(word.lower())
    flag = True
    for i in d2:
        if not d1.get(i) or d1[i] < d2[i]:
            flag = False
    return flag

print(scrabble('BEEGEEK', 'geekbee')) # True


def scrabble1(letters, word):
    letters_dict = {}
    for letter in letters.lower():
        letters_dict[letter] = letters_dict.get(letter, 0) + 1

    word_dict = {}
    for letter in word.lower():
        word_dict[letter] = word_dict.get(letter, 0) + 1

    for letter, amount in word_dict.items():
        if letters_dict.get(letter, 0) < amount:
            return False

    return True

print(scrabble1('othpyn', 'Python')) # True

b = {}
def bank(t, u, count=None):
    if u not in b:
        b[u] = 0

    if t == 'top up':
        b[u] += count
    elif t in {'withdraw', 'pay'}:
        b[u] -= count
    else:
        print(b[u])

sveta = 'id-88753'
timur = 'id-5630'
bank('top up', sveta, 100)
bank('top up', timur, 2000)
bank('withdraw', timur, 100)
bank('top up', sveta, 3000)
bank('withdraw', sveta, 300)
bank('top up', timur, 6000)
bank('pay', timur, 300)
bank('pay', timur, 4000)
bank('pay', timur, 150)
bank('top up', timur, 500)
bank('show balance', timur) # 3950
bank('show balance', sveta) # 2800

def show_top_categories(l, n):
    d = {}
    r = {}
    k = []
    for i in l:
        d[i[0]] = d.setdefault(i[0], 0) + i[1]

    for i in d.items():
        r[i[1]] = i[0]
    for i in range(n):
        m = 0
        for i in r:
            if i > m:
                m = i
        k.append(r.pop(m))
    print(*sorted(k), sep = '\n')

spendings = [
    ('одежда', 4500), ('обувь', 7200),
    ('зоотовары', 1400), ('пекарня', 410),
    ('такси', 350), ('цветы', 2700),
    ('канцтовары', 430), ('фастфуд', 750),
    ('проезд в автобусе', 86),
    ('продукты', 473), ('пекарня', 310),
]
show_top_categories(spendings, 1)
show_top_categories(spendings, 5)
"""
обувь
зоотовары
обувь
одежда
фастфуд
цветы
"""

# def is_subfolder(folder_dict, subfolder, folder):
#     if folder not in folder_dict:
#         return False
#     for child in folder_dict[folder]:
#         if child == subfolder:
#             return True
#         if child in folder_dict:
#             if is_subfolder(folder_dict, subfolder, child):
#                 return True
#     return False


def is_subfolder(folder_dict, subfolder, folder):
    current_folders = [folder]
    while len(current_folders) > 0:
        temp_folders = []
        for folder in current_folders:
            temp_folders.extend(folder_dict.get(folder, []))

        if subfolder in temp_folders:
            return True

        current_folders = temp_folders

    return False

folder_system = {
    'K': ['A', 'B', 'K8', 'K9'],
    'B': ['B1', 'B2', 'B4'],
    'A': ['A7', 'A8', 'A9', 'P', 'R'],
    'P': ['Y', 'P18', 'P21', 'X'],
    'Y': ['U', 'W'],
}
print(is_subfolder(
    folder_system, 'P18', 'B',
)) # False
print(is_subfolder(
    folder_system, 'W', 'X',
)) # False
print(is_subfolder(
    folder_system, 'X', 'K',
)) # True