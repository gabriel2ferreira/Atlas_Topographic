import os
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np
from scipy.spatial import Delaunay
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from mpl_toolkits.mplot3d.art3d import PolyCollection
from mpl_toolkits.mplot3d.art3d import Line3DCollection
from matplotlib import colors as mcolors

# Caminho para o arquivo
coordinates_file_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'coordenadasEspinhoB.txt')

# Coordenadas dos pontos
points = []

# Processar o arquivo de coordenadas
with open(coordinates_file_path, 'r') as coordinates_file:
    lines = coordinates_file.readlines()

elevation = None
for line in lines:
    if line.startswith("Elevation:"):
        elevation = float(line.split(':')[1].strip())
    else:
        coords_str = line.strip()
        if coords_str.startswith('('):
            coords_str = coords_str[1:-1]  # Remover parênteses
            lon, lat, _ = map(float, coords_str.split(', '))
            points.append((lon, lat, elevation))

# Criar o gráfico 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Criar array NumPy com as coordenadas
points_array = np.array([(lon, lat, elevation) for lon, lat, elevation in points])

# Calcular a triangulação de Delaunay
tri = Delaunay(points_array[:, :2])

# Plotar os pontos
ax.scatter(points_array[:, 0], points_array[:, 1], points_array[:, 2], marker='o', color='b')

# Plotar as arestas e faces dos triângulos
for simplex in tri.simplices:
    simplex = np.append(simplex, simplex[0])  # Fechar o polígono
    ax.plot(points_array[simplex, 0], points_array[simplex, 1], points_array[simplex, 2], 'k-')
    verts = [tuple(points_array[simplex, :])]
    tri_verts = Poly3DCollection(verts, alpha=0.2)
    face_color = [plt.cm.viridis(elev / max(points_array[:, 2])) for elev in points_array[simplex, 2]]
    tri_verts.set_facecolor(face_color)
    ax.add_collection3d(tri_verts)
    
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.set_zlabel('Elevation')
ax.set_title('Triangulação de Delaunay e Superfície Fechada')
ax.legend()

# Definir proporções iguais para os eixos
ax.set_box_aspect([1, 1, 0.1])  # Ajustar o valor do último elemento para controlar a escala da elevação

# Maximizar a janela para tela cheia
plt.get_current_fig_manager().window.state('zoomed')

# Exibir o gráfico
plt.show()
