"""
Código para el análisis numérico de convergencia de series
Elaborado para el curso de Métodos Computacionales en Física
"""

import numpy as np
import matplotlib.pyplot as plt

# Configuración de parámetros
n_max = 1000000  # 10^6 términos
muestras_grafico = 1000  # Puntos para visualización

print("Iniciando cálculo de series...")
print(f"Número de términos: {n_max:,}")
print("=" * 50)

# Serie armónica: ∑(1/n)
print("Calculando serie armónica...")
suma_armonica = 0.0
valores_n = np.logspace(1, np.log10(n_max), muestras_grafico).astype(int)
valores_armonica = []

for n in range(1, n_max + 1):
    suma_armonica += 1.0 / n
    
    # Guardar valores para graficar
    if n in valores_n:
        valores_armonica.append((n, suma_armonica))
        print(f"n={n}: Sₙ ≈ {suma_armonica:.6f}")

# Serie de inversos cuadrados: ∑(1/n²)
print("\nCalculando serie de inversos cuadrados...")
suma_cuadrados = 0.0
valores_cuadrados = []

for n in range(1, n_max + 1):
    suma_cuadrados += 1.0 / (n * n)
    
    # Guardar valores para graficar
    if n in valores_n:
        valores_cuadrados.append((n, suma_cuadrados))
        print(f"n={n}: Sₙ ≈ {suma_cuadrados:.6f}")

# Resultados finales
print("\n" + "=" * 50)
print("RESULTADOS FINALES")
print("=" * 50)
print(f"Serie armónica (∑1/n): S ≈ {suma_armonica:.6f}")
print(f"Serie de inversos cuadrados (∑1/n²): S ≈ {suma_cuadrados:.6f}")
print(f"Valor teórico (π²/6): {np.pi**2/6:.6f}")

# Análisis de convergencia
print("\nANÁLISIS:")
print("La serie armónica muestra crecimiento continuo → DIVERGENTE")
print("La serie de inversos cuadrados tiende a π²/6 → CONVERGENTE")


plt.figure(figsize=(12, 5))

# Gráfica serie armónica
plt.subplot(1, 2, 1)
n_vals, s_vals = zip(*valores_armonica)
plt.plot(n_vals, s_vals, 'b-', linewidth=1.5)
plt.xscale('log')
plt.xlabel('n (escala log)')
plt.ylabel('Suma parcial Sₙ')
plt.title('Serie Armónica: ∑(1/n)')
plt.grid(True, alpha=0.3)

# Gráfica serie de inversos cuadrados
plt.subplot(1, 2, 2)
n_vals, s_vals = zip(*valores_cuadrados)
plt.plot(n_vals, s_vals, 'r-', linewidth=1.5)
plt.axhline(y=np.pi**2/6, color='k', linestyle='--', alpha=0.7, label='π²/6')
plt.xscale('log')
plt.xlabel('n (escala log)')
plt.ylabel('Suma parcial Sₙ')
plt.title('Serie: ∑(1/n²)')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('analisis_series.png', dpi=150)
plt.show()

print("\n¡Análisis completado! Gráfica guardada como 'analisis_series.png'")