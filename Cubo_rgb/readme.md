Introducción
Este código crea una visualización 3D de un cubo usando Python y las bibliotecas Matplotlib y NumPy. Lo desarrollé como parte de mi proyecto de visualización de datos para entender cómo representar objetos tridimensionales en un espacio 2D.

Utilicé estas bibliotecas porque:

Matplotlib es la herramienta estándar para visualizaciones en Python
NumPy me ayuda a trabajar con arrays y operaciones matemáticas
Poly3DCollection es específicamente para crear colecciones de polígonos 3D


##########
figura = plt.figure(figsize=(8, 6))
ejes = figura.add_subplot(111, projection='3d')
Creé una figura de 8x6 pulgadas y establecí una proyección 3D porque necesitaba un espacio tridimensional para visualizar el cubo correctamente.
############
Definición de los vértices
puntos = np.array([
    [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],
    [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1]
])
Definí manualmente los 8 vértices del cubo usando coordenadas (x, y, z) porque quería entender la estructura básica de un cubo en el espacio 3D. El cubo está centrado en el origen (0,0,0) con lados de longitud 2.
################
Dibujo de las aristas
color_aristas = 'white'
...
Dibujé cada arista individualmente conectando los vértices porque quería controlar exactamente cómo se vería el contorno del cubo. Usé color azul oscuro para que las aristas fueran visibles pero no demasiado llamativas.
##########
Creación de las caras

caras = [
    [puntos[0], puntos[1], puntos[2], puntos[3]],  # base
    # ... (las otras 5 caras)
]

colores = ['#FF6666', '#66FF66', '#6666FF', '#FFFF66', '#FF66FF', '#66FFFF']
Definí las 6 caras del cubo agrupando 4 vértices para cada una. Elegí colores vibrantes pero diferentes para cada cara para poder distinguirlas fácilmente y porque se parecían a los colores de la referencia que tenía.

##############
Colección de polígonos 3D

coleccion_caras = Poly3DCollection(caras, alpha=0.8, linewidths=1, edgecolors=color_aristas)
coleccion_caras.set_facecolor(colores)
ejes.add_collection3d(coleccion_caras)
Usé Poly3DCollection porque es la forma correcta de agregar polígonos 3D en Matplotlib. El parámetro alpha=0.8 hace las caras ligeramente transparentes para poder ver mejor la estructura del cubo.

##################


 Configuración de ejes y visualización

ejes.set_xlim([-1.5, 1.5])
ejes.set_ylim([-1.5, 1.5])
ejes.set_zlim([-1.5, 1.5])
Establecí límites en los ejes ligeramente más grandes que el cubo para que no se viera cortado y para dejar espacio alrededor.

######
Vista final
ejes.view_init(elev=20, azim=35)
plt.tight_layout()
plt.show()
Ajusté la vista con elevación y azimut para obtener una perspectiva que muestre claramente tres caras del cubo, similar a las representaciones isométricas comunes.