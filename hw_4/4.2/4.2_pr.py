import math
import time
from concurrent.futures import ProcessPoolExecutor


def integrate_range(f, a, b, n_iter):
    """вычисляет интеграл функции f на отрезке [a, b] с n_iter прямоугольниками"""
    acc = 0
    step = (b - a) / n_iter  # ширина одного прямоугольника
    for i in range(n_iter):
        acc += f(a + i * step) * step  # сумма площадей прямоугольников
    return acc  # возвращает приближённое значение интеграла на подотрезке


def integrate(f, a, b, *, n_jobs=1, n_iter=10_000_000):
    """
    f — функция (например, math.cos)
    a, b — границы интегрирования
    n_jobs — число процессов (воркеров)
    n_iter — сколько всего прямоугольников (точность)
    """
    step = (b - a) / n_jobs  # длина одного подотрезка для процесса
    # сколько итераций (прямоугольников) дастся каждому процессу
    part_iter = n_iter // n_jobs

    with ProcessPoolExecutor(max_workers=n_jobs) as executor:
        """создаём пул процессов, каждый процесс берёт по одной задаче"""
        futures = []
        for i in range(n_jobs):
            sub_a = a + i * step      # начало подотрезка
            sub_b = sub_a + step      # конец подотрезка
            futures.append(
                executor.submit(      # отправляем задачу в пул (асинхронно)
                    integrate_range,  # функция, которую нужно выполнить
                    f, sub_a, sub_b, part_iter  # аргументы функции
                )
            )

        # ждём завершения задач и собираем результаты
        results = [f.result() for f in futures]

    return sum(results)  # складываем все части интеграла


# защита от рекурсивного запуска процессов (важно для Windows/macOS)
if __name__ == '__main__':
    for n in range(1, 17):  # перебираем количество процессов от 1 до 16
        start = time.time()
        # запускаем интегрирование
        res = integrate(math.cos, 0, math.pi / 2, n_jobs=n)
        duration = time.time() - start  # замеряем время
        print(
            f"n_jobs = {n:2d} | result = {res:.6f} | time = {duration:.4f}s"
        )  # выводим: сколько процессов, чему равен результат, и сколько времени заняло


# python 4.2_pr.py
