import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Polygon


fig, axes = plt.subplots(2, 3, figsize=(15, 10))
fig.suptitle('Transformaciones de Simetría del Triángulo Equilátero (Grupo D3)', 
             fontsize=16, fontweight='bold')

# Vértices del triángulo equilátero (centrado en el origen)
vertices = np.array([
    [0, 1],           # Vértice superior
    [-np.sqrt(3)/2, -0.5],  # Vértice inferior izquierdo
    [np.sqrt(3)/2, -0.5]    # Vértice inferior derecho
])


colores_vertices = ['red', 'blue', 'green']
color_aristas = 'black'

# Matrices de transformación (representaciones matriciales de D3)
# 1. Identidad
I = np.array([[1, 0], [0, 1]])

# 2. Rotación 120°
theta_120 = 2*np.pi/3
R120 = np.array([
    [np.cos(theta_120), -np.sin(theta_120)],
    [np.sin(theta_120), np.cos(theta_120)]
])

# 3. Rotación 240°
theta_240 = 4*np.pi/3
R240 = np.array([
    [np.cos(theta_240), -np.sin(theta_240)],
    [np.sin(theta_240), np.cos(theta_240)]
])

# 4. Reflexión eje Y (90°)
Fy = np.array([[-1, 0], [0, 1]])

# 5. Reflexión eje 30°
theta_30 = np.pi/6
F30 = np.array([
    [np.cos(2*theta_30), np.sin(2*theta_30)],
    [np.sin(2*theta_30), -np.cos(2*theta_30)]
])

# 6. Reflexión eje 150°
theta_150 = 5*np.pi/6
F150 = np.array([
    [np.cos(2*theta_150), np.sin(2*theta_150)],
    [np.sin(2*theta_150), -np.cos(2*theta_150)]
])

transformaciones = [
    (I, "Identidad (I)"),
    (R120, "Rotación 120° (R)"),
    (R240, "Rotación 240° (R²)"),
    (Fy, "Reflexión Eje Y (F_y)"),
    (F30, "Reflexión Eje 30° (F_30)"),
    (F150, "Reflexión Eje 150° (F_150)")
]

# Función para aplicar transformación y dibujar
def dibujar_triangulo(ax, vertices_transformados, titulo, color_vertices, color_aristas):
    # Dibujar aristas
    triangulo = Polygon(vertices_transformados, closed=True, 
                       fill=False, edgecolor=color_aristas, linewidth=2)
    ax.add_patch(triangulo)
    
    # Dibujar vértices con colores diferentes
    for i, vertice in enumerate(vertices_transformados):
        ax.plot(vertice[0], vertice[1], 'o', markersize=10, 
                color=color_vertices[i], label=f'V{i+1}')
    
   
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.set_title(titulo, fontweight='bold')
    ax.axhline(y=0, color='k', linestyle='--', alpha=0.3)
    ax.axvline(x=0, color='k', linestyle='--', alpha=0.3)

for i, (transformacion, nombre) in enumerate(transformaciones):
    fila = i // 3
    columna = i % 3
    ax = axes[fila, columna]
    
    
    vertices_transformados = vertices @ transformacion.T  # Multiplicación matricial
    
    dibujar_triangulo(ax, vertices_transformados, nombre, colores_vertices, color_aristas)


plt.figlegend(['Vértice 1 (Rojo)', 'Vértice 2 (Azul)', 'Vértice 3 (Verde)', 'Aristas'], 
              loc='lower center', ncol=4, bbox_to_anchor=(0.5, -0.05))

plt.tight_layout()
plt.show()


print("Matrices de transformación:")
print("="*50)
for i, (transformacion, nombre) in enumerate(transformaciones):
    print(f"\n{nombre}:")
    print(np.round(transformacion, 3))