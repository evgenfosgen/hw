import time
from multiprocessing import Process


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


if __name__ == '__main__':  # нужен, чтобы предотвратить бесконечный запуск процессов при использовании
    N = 100_000
    NUM_CALLS = 10
    processes = []

    start = time.time()
    for _ in range(NUM_CALLS):
        t = Process(target=fib, args=(N,))
        processes.append(t)
        t.start()

    for t in processes:
        t.join()
    """""
    Тут ждём завершения всех потоков.
    Без join() программа могла бы закончиться раньше, чем потоки успеют завершиться.
    """""
    end = time.time()

    print(f"время (процессы): {end - start:.4f}")
# python 4.1_pr.py
