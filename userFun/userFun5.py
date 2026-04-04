def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

def is_sorted(names):
    new_names = names.copy()
    new_names.sort()

    if names == new_names:
        return True
    else:
        return False

# Проверяем, что строки одинаковой длинны и отличаются только одним символом
def is_one_away(word1, word2):
    return len(word1) == len(word2) and 1 == sum(c1 != c2 for c1, c2 in zip(word1, word2))

number = 5
if is_even(number):
    print('Это число чётное.')
else:
    print('Это число нечётное.')

print(is_sorted(['Александра', 'Владимир', 'Борис', 'Илья', 'Мария']))

print(is_one_away('hide', 'ride'))
