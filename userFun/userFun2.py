def draw_box(height, width):    # функция принимает два параметра
    for i in range(height):
        print('*' * width)

def print_hello(n):
    print('Hello' * n)

def print_text(txt, n): # В функцию передаем параметрические (формальные) параметры txt и n
    print(txt * n)

# Функция определения местного времени по московскому
def print_perm_time_call(msc_time):
    t = msc_time.split(':')
    print(f'Созвон будет в {(int(t[0]) + 4):02d}:{t[1]}.')

draw_box(3, 3)
print()
draw_box(5, 5)
print()
draw_box(4, 10)
print()

print_hello(5)

print()
print_text('text', 4) # При вызове передаем аргументы (фактические параметры)