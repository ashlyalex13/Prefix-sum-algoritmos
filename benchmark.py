"""
Benchmarking: Ingenua O(n) vs Prefix Sum O(1)
Autor: Ashly Hernandez - 2363157-2724
Materia: Análisis y Diseño de Algoritmos
"""

import time
import random
from algoritmos import suma_rango_ingenua, construir_prefix_sum, suma_rango_optimizada


def run_benchmark():
    tamanios = [1_000, 10_000, 100_000, 500_000, 1_000_000]
    num_consultas = 5_000

    print(f"\n{'n':>12}  {'Ingenua (ms)':>14}  {'Optimizada (ms)':>16}  {'Speedup':>9}")
    print("-" * 58)

    for n in tamanios:
        arr = [random.randint(1, 1000) for _ in range(n)]
        prefix = construir_prefix_sum(arr)

        consultas = []
        for _ in range(num_consultas):
            l = random.randint(0, n - 2)
            r = random.randint(l, n - 1)
            consultas.append((l, r))

        t0 = time.perf_counter()
        for l, r in consultas:
            suma_rango_ingenua(arr, l, r)
        t_ing = (time.perf_counter() - t0) * 1000

        t0 = time.perf_counter()
        for l, r in consultas:
            suma_rango_optimizada(prefix, l, r)
        t_opt = (time.perf_counter() - t0) * 1000

        speedup = t_ing / t_opt if t_opt > 0 else 0
        print(f"{n:>12,}  {t_ing:>14.2f}  {t_opt:>16.4f}  {speedup:>8.1f}x")


if __name__ == "__main__":
    run_benchmark()