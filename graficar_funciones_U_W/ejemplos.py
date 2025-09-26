import numpy as np
import matplotlib.pyplot as plt

# Configuración básica
t = np.linspace(0, 4*np.pi, 500)

# Crear figura con 3 ejemplos distintos
fig, axes = plt.subplots(3, 2, figsize=(15, 12))

# =============================================
# EJEMPLO 1: U y W con misma amplitud (caso base)
# =============================================
A1 = 1.0
B1 = 1.0

U1 = A1 * (np.cos(t) + np.sin(t))
W1 = B1 * (np.cos(t) - np.sin(t))
suma1 = U1 + W1

# Gráfica de las funciones
axes[0,0].plot(t, U1, 'r-', label=f'U = {A1}(cos(t) + sin(t))', alpha=0.7)
axes[0,0].plot(t, W1, 'b-', label=f'W = {B1}(cos(t) - sin(t))', alpha=0.7)
axes[0,0].plot(t, suma1, 'g-', label='U + W', linewidth=2)
axes[0,0].set_title('Ejemplo 1: Amplitudes iguales (A=B=1)')
axes[0,0].set_ylabel('Amplitud')
axes[0,0].legend()
axes[0,0].grid(True, alpha=0.3)

# Análisis de la suma
teorico1 = (A1 + B1) * np.cos(t) + (A1 - B1) * np.sin(t)
axes[0,1].plot(t, suma1, 'g-', label='U + W (real)', linewidth=2)
axes[0,1].plot(t, teorico1, 'k--', label='U + W (teórico)', alpha=0.7)
axes[0,1].set_title(f'Suma: {A1+B1}cos(t) + {A1-B1}sin(t)')
axes[0,1].set_ylabel('Amplitud')
axes[0,1].legend()
axes[0,1].grid(True, alpha=0.3)

# =============================================
# EJEMPLO 2: U y W con amplitudes diferentes
# =============================================
A2 = 2.0
B2 = 0.5

U2 = A2 * (np.cos(t) + np.sin(t))
W2 = B2 * (np.cos(t) - np.sin(t))
suma2 = U2 + W2

axes[1,0].plot(t, U2, 'r-', label=f'U = {A2}(cos(t) + sin(t))', alpha=0.7)
axes[1,0].plot(t, W2, 'b-', label=f'W = {B2}(cos(t) - sin(t))', alpha=0.7)
axes[1,0].plot(t, suma2, 'g-', label='U + W', linewidth=2)
axes[1,0].set_title('Ejemplo 2: Amplitudes diferentes (A=2, B=0.5)')
axes[1,0].set_ylabel('Amplitud')
axes[1,0].legend()
axes[1,0].grid(True, alpha=0.3)

teorico2 = (A2 + B2) * np.cos(t) + (A2 - B2) * np.sin(t)
axes[1,1].plot(t, suma2, 'g-', label='U + W (real)', linewidth=2)
axes[1,1].plot(t, teorico2, 'k--', label='U + W (teórico)', alpha=0.7)
axes[1,1].set_title(f'Suma: {A2+B2}cos(t) + {A2-B2}sin(t)')
axes[1,1].set_ylabel('Amplitud')
axes[1,1].legend()
axes[1,1].grid(True, alpha=0.3)

# =============================================
# EJEMPLO 3: U y W con fases desplazadas
# =============================================
A3 = 1.0
B3 = 1.0
fase = np.pi/4  # Desplazamiento de fase

U3 = A3 * (np.cos(t) + np.sin(t))
W3 = B3 * (np.cos(t - fase) - np.sin(t - fase))  # W con fase desplazada
suma3 = U3 + W3

axes[2,0].plot(t, U3, 'r-', label=f'U = {A3}(cos(t) + sin(t))', alpha=0.7)
axes[2,0].plot(t, W3, 'b-', label=f'W con fase π/4', alpha=0.7)
axes[2,0].plot(t, suma3, 'g-', label='U + W', linewidth=2)
axes[2,0].set_title('Ejemplo 3: W con fase desplazada π/4')
axes[2,0].set_xlabel('Tiempo (t)')
axes[2,0].set_ylabel('Amplitud')
axes[2,0].legend()
axes[2,0].grid(True, alpha=0.3)

axes[2,1].plot(t, suma3, 'g-', label='U + W (con fase)', linewidth=2)
axes[2,1].plot(t, 2*np.cos(t), 'k--', label='2cos(t) (referencia)', alpha=0.5)
axes[2,1].set_title('Suma con fase desplazada')
axes[2,1].set_xlabel('Tiempo (t)')
axes[2,1].set_ylabel('Amplitud')
axes[2,1].legend()
axes[2,1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# =============================================
# ANÁLISIS COMPARATIVO
# =============================================
print("="*70)
print("ANÁLISIS COMPARATIVO DE LOS TRES EJEMPLOS")
print("="*70)

# Calcular características de cada suma
def analizar_suma(nombre, suma, t):
    amplitud_max = np.max(suma)
    amplitud_min = np.min(suma)
    amplitud_pico = (amplitud_max - amplitud_min) / 2
    valor_rms = np.sqrt(np.mean(suma**2))
    
    print(f"\n{nombre}:")
    print(f"  Amplitud máxima: {amplitud_max:.3f}")
    print(f"  Amplitud mínima: {amplitud_min:.3f}")
    print(f"  Amplitud pico-pico: {amplitud_pico*2:.3f}")
    print(f"  Valor RMS: {valor_rms:.3f}")
    
    return amplitud_pico, valor_rms

# Analizar cada caso
p1, rms1 = analizar_suma("EJEMPLO 1 - Amplitudes iguales", suma1, t)
p2, rms2 = analizar_suma("EJEMPLO 2 - Amplitudes diferentes", suma2, t)
p3, rms3 = analizar_suma("EJEMPLO 3 - Fase desplazada", suma3, t)

# =============================================
# GRÁFICA COMPARATIVA FINAL
# =============================================
plt.figure(figsize=(12, 8))

plt.plot(t, suma1, 'g-', label='Ej1: A=B=1 → 2cos(t)', linewidth=2)
plt.plot(t, suma2, 'b-', label='Ej2: A=2, B=0.5 → 2.5cos(t) + 1.5sin(t)', linewidth=2)
plt.plot(t, suma3, 'r-', label='Ej3: W con fase π/4', linewidth=2)

plt.title('COMPARACIÓN: Tres tipos diferentes de suma U + W')
plt.xlabel('Tiempo (t)')
plt.ylabel('Amplitud')
plt.legend()
plt.grid(True, alpha=0.3)

# Añadir anotaciones con los resultados
plt.annotate(f'Amplitud: {p1*2:.2f}', xy=(np.pi, suma1[125]), 
             xytext=(np.pi+1, suma1[125]+0.5),
             arrowprops=dict(arrowstyle='->', color='green'))

plt.annotate(f'Amplitud: {p2*2:.2f}', xy=(2*np.pi, suma2[250]), 
             xytext=(2*np.pi+1, suma2[250]+1),
             arrowprops=dict(arrowstyle='->', color='blue'))

plt.annotate(f'Amplitud: {p3*2:.2f}', xy=(3*np.pi, suma3[375]), 
             xytext=(3*np.pi+1, suma3[375]-1),
             arrowprops=dict(arrowstyle='->', color='red'))

plt.show()

