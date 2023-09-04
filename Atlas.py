import os
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from scipy.spatial import ConvexHull
import numpy as np

# Caminho para o arquivo de coordenadas
coordinates_file_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'coordinates_by_elevation.txt')

# Lendo as últimas 100 linhas do arquivo
with open(coordinates_file_path, 'r') as coordinates_file:
    lines = coordinates_file.readlines()
    last_100_lines = lines[-100:]

# Coordenadas dos pontos
points = []

# Processar as linhas do arquivo
elevation = None
for line in last_100_lines:
    if line.startswith("Elevation:"):
        elevation = float(line.split(':')[1].strip())
    else:
        coords_str = line.strip()
        if coords_str.startswith('('):
            coords_str = coords_str[1:-1]  # Remover parênteses
            lon, lat, _ = map(float, coords_str.split(', '))
            points.append((lon, lat, elevation))

# Criar uma lista separada para cada elevação
elevations = set([point[2] for point in points])
elevation_points_dict = {elevation: [] for elevation in elevations}

for point in points:
    elevation_points_dict[point[2]].append(point)

# Criar o gráfico 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plotar os pontos e criar a superfície para cada elevação
for elevation, elevation_points in elevation_points_dict.items():
    lon, lat, _ = zip(*elevation_points)
    ax.scatter(lon, lat, [elevation] * len(lon), c=[elevation] * len(lon), cmap='viridis', label=f'Elevation: {elevation}')

    if len(lon) > 2:  # Precisa de pelo menos 3 pontos para criar a superfície
        hull_points = np.array(elevation_points)[:, :2]  # Coordenadas de lon e lat
        hull = ConvexHull(hull_points)
        vertices = hull_points[hull.vertices]
        vertices = np.column_stack((vertices, np.full(vertices.shape[0], elevation)))
        poly = Poly3DCollection([vertices], facecolors=[plt.cm.viridis(elevation)], alpha=0.5)
        ax.add_collection3d(poly)

ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.set_zlabel('Elevation')
ax.set_title('Coordenadas em 3D por Elevação')
ax.legend()
plt.show()
