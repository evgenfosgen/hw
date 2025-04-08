import time


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


N = 100000
NUM_CALLS = 10

start = time.time()
results = []

for _ in range(NUM_CALLS):
    results.append(fib(N))

end = time.time()

print(f"время : {end - start:.4f}")
# python 4.1.py
