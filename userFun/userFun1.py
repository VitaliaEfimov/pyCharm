# print_message() # NameError: name 'print_message' is not defined. Вызов функции не может быть до объявления функции

# Объявление функции - не вызов!
def print_message(): # Заголовок функции (подпрограмма)
    print('Я - Артур,') # Тело функции
    print('король британцев. ')

def do_nothing():
    pass # Ничего не делать - заглушка.

print_message() # Вызов функции
do_nothing()

#    print('Это очень важная тема!') # 3 пробела IndentationError: unexpected indent