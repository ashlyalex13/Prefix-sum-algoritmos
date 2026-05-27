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
    tiempos_ingenua = []
    tiempos_opt = []


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

        tiempos_ingenua.append(t_ing)
        tiempos_opt.append(t_opt)

        speedup = t_ing / t_opt if t_opt > 0 else 0
        print(f"{n:>12,}  {t_ing:>14.2f}  {t_opt:>16.4f}  {speedup:>8.1f}x")

    return tamanios, tiempos_ingenua, tiempos_opt


import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def graficar(tamanios, tiempos_ingenua, tiempos_opt):
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))
    fig.suptitle("Benchmark: Ingenua O(n) vs Prefix Sum O(1)", fontsize=14, fontweight="bold")

    ax1 = axes[0]
    ax1.plot(tamanios, tiempos_ingenua, "o-", color="#E24B4A", linewidth=2.5, label="Ingenua O(n)")
    ax1.plot(tamanios, tiempos_opt, "s-", color="#1D9E75", linewidth=2.5, label="Prefix Sum O(1)")
    ax1.set_xlabel("Tamaño del arreglo (n)")
    ax1.set_ylabel("Tiempo total (ms)")
    ax1.set_title("Tiempo de ejecución")
    ax1.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f"{int(x):,}"))
    ax1.legend()
    ax1.grid(True, linestyle="--", alpha=0.4)

    ax2 = axes[1]
    speedups = [i / o if o > 0 else 0 for i, o in zip(tiempos_ingenua, tiempos_opt)]
    ax2.bar(range(len(tamanios)), speedups, color="#378ADD", alpha=0.85)
    ax2.set_xticks(range(len(tamanios)))
    ax2.set_xticklabels([f"{n//1000}K" for n in tamanios])
    ax2.set_xlabel("Tamaño del arreglo (n)")
    ax2.set_ylabel("Veces más rápido")
    ax2.set_title("Speedup (Ingenua / Prefix Sum)")
    for i, v in enumerate(speedups):
        ax2.text(i, v + 0.5, f"{v:.0f}x", ha="center", fontsize=9, fontweight="bold")
    ax2.grid(True, linestyle="--", alpha=0.4, axis="y")

    plt.tight_layout()
    plt.savefig("benchmark_resultado.png", dpi=150, bbox_inches="tight")
    plt.show()
    print("\n✓ Gráfica guardada en: benchmark_resultado.png")


if __name__ == "__main__":
    tamanios, t_ing, t_opt = run_benchmark()
    graficar(tamanios, t_ing, t_opt)