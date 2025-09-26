import numpy as np
import matplotlib.pyplot as plt

# Definir el tiempo t de 0 a 4*pi con 100 puntos
t = np.linspace(0, 4*np.pi, 100)

# Definir las funciones U y W 
U = 3 *(np.cos(t) + np.sin(t))
W = np.cos(t) - np.sin(t)

plt.figure(figsize=(10, 6))
plt.plot(t, U, 'r-', label='U = cos(t) + sin(t)', linewidth=2)
plt.plot(t, W, 'b-', label='W = cos(t) - sin(t)', linewidth=2)


plt.title('Gráfica de U y W vs tiempo', fontsize=14)
plt.xlabel('Tiempo (t)', fontsize=12)
plt.ylabel('Valor', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

# Ajustar los límites del eje y para mejor visualización
plt.ylim(-2, 2)
plt.show()