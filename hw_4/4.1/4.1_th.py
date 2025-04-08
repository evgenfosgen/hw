import time
from threading import Thread


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


N = 100_000
NUM_CALLS = 10
threads = []

start = time.time()
for _ in range(NUM_CALLS):
    t = Thread(target=fib, args=(N,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
"""""
Тут ждём завершения всех потоков.
Без join() программа могла бы закончиться раньше, чем потоки успеют завершиться.
"""""
end = time.time()

print(f"время (потоки): {end - start:.4f}")
# python 4.1_th.py
