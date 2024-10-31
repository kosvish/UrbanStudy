# ---------------------------------------------------------------------------------------------------------------------
# 1. Асинхронность. Понятия
# ---------------------------------------------------------------------------------------------------------------------
import time
import asyncio


# Асинхронное программирование
def notification_sync():
    time.sleep(10)
    print("До доставки осталось 10 минут")


# корутины
async def notification_async():
    await asyncio.sleep(10)
    print("До доставки осталось 10 минут")


# для того что бы запустить корутину её нужно "заавейтить" с помощью оператора await
async def main():
    print("Жду уведомление...")
    await notification_async()
    print("Уведомление получено!")


asyncio.run(main())


# Асинхронные задачи

async def main():
    print("Создаю задачу")
    task = asyncio.create_task(notification_async())  # Запускаем задачу
    print("Продолжаем выполнять другие задачи")
    await task  # Ожидаем завершение задачи


asyncio.run(main())

# ---------------------------------------------------------------------------------------------------------------------
# 2. Асинхронность. Понятия
# ---------------------------------------------------------------------------------------------------------------------

# Пример: синхронный подход
import time


def task1():
    time.sleep(2)
    print("Задача 1 завершена")


def task2():
    time.sleep(4)
    print("Задача 2 завершена")


def main():
    task1()
    task2()


start = time.time()
main()
print(f"Общее время: {time.time() - start:.2f} секунд")

# Асинхронный подход

import asyncio


async def task1_async():
    await asyncio.sleep(2)
    print("Задача 1 завершена")


async def task2_async():
    await asyncio.sleep(4)
    print("Задача 2 завершена")


async def main():
    print("Запускаем задачи...")
    task1_coroutine = asyncio.create_task(task1())
    task2_coroutine = asyncio.create_task(task2())

    await task1_coroutine
    await task2_coroutine
    print("Все задачи завершены")


start = time.time()
asyncio.run(main())
print(f"Общее время: {time.time() - start:.2f} секунд")
