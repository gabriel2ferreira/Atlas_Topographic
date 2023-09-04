import os
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Caminho para o arquivo
coordinates_file_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'coordinates_above_260.txt')

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

# Criar uma estrutura de dados para agrupar as coordenadas por elevação
elevation_points = {}
for lon, lat, elevation in points:
    if elevation is not None:
        if elevation not in elevation_points:
            elevation_points[elevation] = []
        elevation_points[elevation].append((lon, lat, elevation))

# Plotar as áreas em 3D
for elevation, elev_points in elevation_points.items():
    xs = [lon for lon, _, _ in elev_points]
    ys = [lat for _, lat, _ in elev_points]
    zs = [elevation for _, _, elevation in elev_points]
    ax.scatter(xs, ys, zs, marker='o', label=f'Elevation: {elevation}')

ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.set_zlabel('Elevation')
ax.set_title('Pontos 3D por Elevação')
ax.legend()

# Definir proporções iguais para os eixos
ax.set_box_aspect([1, 1, 0.1])  # Ajuste o valor do último elemento para controlar a escala da elevação

plt.show()
