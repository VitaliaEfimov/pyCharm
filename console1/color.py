from colorama import Fore, Back, Style, init

init()  # инициализация библиотеки для поддержки разных ОС

# вывод разноцветного текста
print(Fore.RED + "Красный текст")
print(Fore.GREEN + "Зелёный текст")
print(Fore.BLUE + "Синий текст")

# Фоновые цвета
print(Back.YELLOW + "Текст с жёлтым фоном")

# Сброс всех настроек
print(Style.RESET_ALL + "Вернули всё в исходное состояние.")