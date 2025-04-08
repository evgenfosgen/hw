import math
import time
from concurrent.futures import ThreadPoolExecutor


def integrate_range(f, a, b, n_iter):
    acc = 0
    step = (b - a) / n_iter
    for i in range(n_iter):
        acc += f(a + i * step) * step
    return acc


def integrate(f, a, b, *, n_jobs=1, n_iter=10_000_000):
    step = (b - a) / n_jobs
    part_iter = n_iter // n_jobs

    # все то же самое как в процессах кроме этого
    with ThreadPoolExecutor(max_workers=n_jobs) as executor:
        futures = []
        for i in range(n_jobs):
            sub_a = a + i * step
            sub_b = sub_a + step
            futures.append(executor.submit(
                integrate_range, f, sub_a, sub_b, part_iter))

        results = [f.result() for f in futures]

    return sum(results)


if __name__ == '__main__':
    for n in range(1, 17):
        start = time.time()
        res = integrate(math.cos, 0, math.pi / 2, n_jobs=n)
        duration = time.time() - start
        print(
            f"n_jobs = {n:2d} | result = {res:.6f} | time = {duration:.4f}s")


# python 4.2_th.py
