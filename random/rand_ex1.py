from random import *

def coin_flip():
    if random()>0.5:
        return 'Орел'
    else:
        return 'Решка'

print(coin_flip())
print(coin_flip())
print(coin_flip())
print(coin_flip())
print()

def dice_flip():
    return randint(1, 6)

print(dice_flip())
print(dice_flip())
print(dice_flip())
print(dice_flip())
print(dice_flip())
print(dice_flip())
print()

def generate_password(n):
    s = ''
    for i in range(n):
        if random() > 0.5:
            s += chr(randrange(65, 91))
        else:
            s += chr(randrange(97, 123))

    return s

print(generate_password(5))
print(generate_password(7))
print(generate_password(10))
print(generate_password(15))
print(generate_password(20))
print()

from random import *

def generate_lottery_ticket():
    s = set()
    while len(s) < 7:
        n = randint(1, 49)
        if n not in s:
            s.add(n)
    r = [str(i) for i in sorted(s)]
    return ' '.join(r)

print(generate_lottery_ticket())
print(generate_lottery_ticket())
print(generate_lottery_ticket())


