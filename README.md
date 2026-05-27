# Prefix Sum: De O(n) a O(1)

Proyecto final de **Análisis y Diseño de Algoritmos**.

Este proyecto demuestra cómo la técnica de **Prefix Sum (Suma de Prefijos)** permite optimizar consultas de suma de rangos, reduciendo la complejidad temporal de:

- Implementación ingenua: `O(n)` por consulta
- Implementación optimizada: `O(1)` por consulta

mediante precomputación.

---

# Integrante

- Ashly Hernandez — 2363157-2724

---

# Objetivo

Investigar, implementar y demostrar cómo una técnica matemática de precomputación puede transformar un problema lineal en uno de tiempo constante, permitiendo escalabilidad masiva.

---

# Estructura del Proyecto

```text
Prefix-sum-algoritmos/
│
├── algoritmos.py
├── benchmark.py
├── benchmark_resultado.png
├── documento.tex
├── documento.pdf
└── README.md
```

---

# Archivos

## `algoritmos.py`

Contiene:

- Implementación ingenua `O(n)`
- Implementación optimizada con Prefix Sum `O(1)`
- Verificación de correctitud

---

## `benchmark.py`

Realiza:

- generación de arreglos aleatorios,
- benchmarking,
- medición de tiempos,
- cálculo de speedup,
- generación de gráficas.

---

## `documento.tex` y `documento.pdf`

Documento técnico en LaTeX con:

- análisis matemático,
- demostración de complejidad,
- benchmarking,
- aplicaciones reales.

---

# Cómo ejecutar

## 1. Verificación de correctitud

```bash
python algoritmos.py
```

---

## 2. Benchmarking

```bash
python benchmark.py
```

---

# Resultados

Las pruebas muestran mejoras superiores a:

## 30.000x más rápido

para arreglos de tamaño:

```text
n = 1.000.000
```

---

# Tecnologías utilizadas

- Python 3
- Matplotlib
- LaTeX

---

# Aplicaciones reales

- Bases de datos SQL
- Business Intelligence
- Computer Vision
- Sistemas de analítica masiva

---

# Repositorio

https://github.com/ashlyalex13/Prefix-sum-algoritmos
