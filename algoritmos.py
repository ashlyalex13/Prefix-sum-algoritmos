"""
Prefix Sum (Suma de Rangos)
Autor: Ashly Hernandez - 2363157-2724
Materia: Análisis y Diseño de Algoritmos
"""


# IMPLEMENTACIÓN INGENUA — O(n) por consulta

def suma_rango_ingenua(arr, l, r):
    """
    Calcula la suma de arr[l..r] recorriendo todos los elementos.
    Complejidad: O(n) por consulta.
    """
    total = 0
    for i in range(l, r + 1):
        total += arr[i]
    return total

# IMPLEMENTACIÓN OPTIMIZADA — O(1) por consulta

def construir_prefix_sum(arr):
    """
    Precomputa el arreglo de sumas prefijas en O(n).
    prefix[0] = 0
    prefix[i] = prefix[i-1] + arr[i-1]
    """
    n = len(arr)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + arr[i]
    return prefix


def suma_rango_optimizada(prefix, l, r):
    """
    Consulta la suma de arr[l..r] en tiempo O(1).
    Fórmula: prefix[r+1] - prefix[l]
    """
    return prefix[r + 1] - prefix[l]

# VERIFICACIÓN DE CORRECTITUD

def verificar_correctitud():
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    prefix = construir_prefix_sum(arr)

    casos = [(0, 4), (2, 7), (0, 9), (3, 3), (1, 8)]
    print(f"Arreglo: {arr}\n")
    for l, r in casos:
        r1 = suma_rango_ingenua(arr, l, r)
        r2 = suma_rango_optimizada(prefix, l, r)
        ok = "✓" if r1 == r2 else "✗"
        print(f"arr[{l}..{r}] -> Ingenua: {r1}  Optimizada: {r2}  {ok}")


if __name__ == "__main__":
    verificar_correctitud()