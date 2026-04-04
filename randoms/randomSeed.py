import random
import threading
import time

# Глобальная переменная для синхронизации
result = [None, None]
start_event = threading.Event()


def generate_random(index, seed_value):
    """Функция для генерации случайного числа с заданным seed"""
    # Ожидаем сигнала для одновременного старта
    start_event.wait()

    # Устанавливаем seed для детерминированной генерации
    random.seed(seed_value)

    # Генерируем случайное число
    number = random.randint(1, 100)
    result[index] = number
    print(f"Поток {index}: сгенерировано число {number} (seed={seed_value})")
    print()


def main():
    # Используем одинаковый seed для обоих потоков
    common_seed = 42

    # Создаем потоки
    thread1 = threading.Thread(target=generate_random, args=(0, common_seed))
    thread2 = threading.Thread(target=generate_random, args=(1, common_seed))

    # Запускаем потоки
    thread1.start()
    thread2.start()

    # Даем потокам подготовиться и одновременно стартуем
    time.sleep(0.1)
    start_event.set()

    # Ждем завершения потоков
    thread1.join()
    thread2.join()

    # Проверяем совпадение
    if result[0] == result[1]:
        print(f"\n✅ Успех! Числа совпадают: {result[0]} = {result[1]}")
    else:
        print(f"\n❌ Ошибка! Числа не совпадают: {result[0]} ≠ {result[1]}")


if __name__ == "__main__":
    main()