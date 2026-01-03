import time
import sys
from colorama import Fore, Back, Style, init

print(Fore.GREEN, end = '')


def progress_bar(iteration, total, bar_length=50):
    percent = float(iteration) / total
    arrow = '=' * int(round(percent * bar_length) - 1) + '>'
    spaces = ' ' * (bar_length - len(arrow))

    # Обновляем строку состояния прямо в консоли
    sys.stdout.write(f"\rПроцесс загрузки: [{arrow}{spaces}] {int(percent * 100)}%")
    sys.stdout.flush()


if __name__ == "__main__":
    for i in range(101):
        progress_bar(i, 100)
        time.sleep(0.2)  # задержка для наглядности процесса
    print("\nЗагрузка завершена!")