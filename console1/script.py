import time
import sys
from colorama import Fore, Back, Style, init

print(Fore.RED, end = '')

def progress_bar(iteration):
    # Обновляем строку состояния прямо в консоли
    sys.stdout.write(f"\rПроцесс загрузки: [{iteration}%]")
    sys.stdout.flush()


if __name__ == "__main__":
    for i in range(101):
        progress_bar(i)
        time.sleep(0.1)  # задержка для наглядности процесса
    print("\nЗагрузка завершена!")

