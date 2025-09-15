
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Configurar la figura
figura = plt.figure(figsize=(8, 6))
ejes = figura.add_subplot(111, projection='3d')

# Definir los puntos del cubo
puntos = np.array([
    [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],  # base
    [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1]       # parte superior
])

# Conectar los puntos para formar las aristas 
color_aristas = 'white'  

# Cara inferior
ejes.plot([puntos[0][0], puntos[1][0]], [puntos[0][1], puntos[1][1]], [puntos[0][2], puntos[1][2]], color=color_aristas, linewidth=2)
ejes.plot([puntos[1][0], puntos[2][0]], [puntos[1][1], puntos[2][1]], [puntos[1][2], puntos[2][2]], color=color_aristas, linewidth=2)
ejes.plot([puntos[2][0], puntos[3][0]], [puntos[2][1], puntos[3][1]], [puntos[2][2], puntos[3][2]], color=color_aristas, linewidth=2)
ejes.plot([puntos[3][0], puntos[0][0]], [puntos[3][1], puntos[0][1]], [puntos[3][2], puntos[0][2]], color=color_aristas, linewidth=2)

# Cara superior
ejes.plot([puntos[4][0], puntos[5][0]], [puntos[4][1], puntos[5][1]], [puntos[4][2], puntos[5][2]], color=color_aristas, linewidth=2)
ejes.plot([puntos[5][0], puntos[6][0]], [puntos[5][1], puntos[6][1]], [puntos[5][2], puntos[6][2]], color=color_aristas, linewidth=2)
ejes.plot([puntos[6][0], puntos[7][0]], [puntos[6][1], puntos[7][1]], [puntos[6][2], puntos[7][2]], color=color_aristas, linewidth=2)
ejes.plot([puntos[7][0], puntos[4][0]], [puntos[7][1], puntos[4][1]], [puntos[7][2], puntos[4][2]], color=color_aristas, linewidth=2)

# Aristas verticales
ejes.plot([puntos[0][0], puntos[4][0]], [puntos[0][1], puntos[4][1]], [puntos[0][2], puntos[4][2]], color=color_aristas, linewidth=2)
ejes.plot([puntos[1][0], puntos[5][0]], [puntos[1][1], puntos[5][1]], [puntos[1][2], puntos[5][2]], color=color_aristas, linewidth=2)
ejes.plot([puntos[2][0], puntos[6][0]], [puntos[2][1], puntos[6][1]], [puntos[2][2], puntos[6][2]], color=color_aristas, linewidth=2)
ejes.plot([puntos[3][0], puntos[7][0]], [puntos[3][1], puntos[7][1]], [puntos[3][2], puntos[7][2]], color=color_aristas, linewidth=2)

# Añadir caras con colores más similares a la referencia
caras = [
    [puntos[0], puntos[1], puntos[2], puntos[3]],  # base
    [puntos[4], puntos[5], puntos[6], puntos[7]],  # superior
    [puntos[0], puntos[1], puntos[5], puntos[4]],  # frontal
    [puntos[2], puntos[3], puntos[7], puntos[6]],  # trasera
    [puntos[1], puntos[2], puntos[6], puntos[5]],  # derecha
    [puntos[0], puntos[3], puntos[7], puntos[4]]   # izquierda
]


colores = [
    '#FF6666',  # Rojo claro
    '#66FF66',  # Verde claro
    '#6666FF',  # Azul claro
    '#FFFF66',  # Amarillo
    '#FF66FF',  # Rosa
    '#66FFFF'   # Cian
]

# Crear la colección de polígonos 3D con transparencia reducida
coleccion_caras = Poly3DCollection(caras, alpha=0.8, linewidths=1, edgecolors=color_aristas)
coleccion_caras.set_facecolor(colores)

# Añadir la colección al gráfico
ejes.add_collection3d(coleccion_caras)

# Configurar los ejes 
ejes.set_xlim([-1.5, 1.5])
ejes.set_ylim([-1.5, 1.5])
ejes.set_zlim([-1.5, 1.5])

# Etiquetas de ejes 
ejes.set_xlabel('Eje X')
ejes.set_ylabel('Eje Y')
ejes.set_zlabel('Eje Z')

# Título
plt.title('Mi Cubo 3D - Proyecto de Visualización', fontsize=14, pad=20)

# Ajustar la vista
ejes.view_init(elev=20, azim=35)

# Mostrar la figura
plt.tight_layout()
plt.show()