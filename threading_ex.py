import threading
import time
import sys
import os

shared_variable = 0  # Общая переменная
lock = threading.Lock()  # Блокировка для синхронизации доступа


# Поток обновления переменной
def update_thread():
    global shared_variable
    while True:
        with lock:  # Обеспечиваем безопасный доступ к переменной
            shared_variable += 9
        time.sleep(0.1)  # Пауза 100 мс


# Поток вывода значения переменной
def display_thread():
    global shared_variable
    while True:
        with lock:  # Обеспечиваем безопасный доступ к переменной
            value = f"Current Value: {shared_variable}"
        print(f'\r{value}', end='', flush=True)  # Выводим значение, обновляя одну строку
        time.sleep(0.3)  # Пауза 300 мс


if __name__ == "__main__":
    t1 = threading.Thread(target=update_thread)
    t2 = threading.Thread(target=display_thread)

    t1.start()
    t2.start()

    try:
        while True:
            pass  # Основная нить ничего не делает, потоки работают автономно
    except KeyboardInterrupt:
        sys.exit('Программа завершена')
        # input("Нажмите Enter для выхода...\n")
        # os.kill(os.getpid(), signal.SIGINT)
