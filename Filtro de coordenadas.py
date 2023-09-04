import os
from shapely.geometry import Point, Polygon

# Caminhos para os arquivos
coordinates_file_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'coordinates_above_260.txt')
outras_coordenadas_file_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'Outras_coordenadas_modified.txt')

# Ler as coordenadas do polígono do arquivo "Outras_coordenadas_modified"
polygon_coords = []
with open(outras_coordenadas_file_path, 'r') as outras_coordenadas_file:
    lines = outras_coordenadas_file.readlines()
    for line in lines:
        coords_str = line.strip().strip('()').split(',')
        lon = float(coords_str[0])
        lat = float(coords_str[1])
        polygon_coords.append((lon, lat))

# Criar um objeto Polygon com as coordenadas do polígono
polygon = Polygon(polygon_coords)

# Lista para armazenar as coordenadas dentro do polígono
coordenadas_filtradas = []

# Ler as coordenadas do arquivo "coordinates_above_260"
with open(coordinates_file_path, 'r') as coordinates_file:
    lines = coordinates_file.readlines()
    for line in lines:
        coords_str = line.strip().strip('()').split(',')
        lon = float(coords_str[0])
        lat = float(coords_str[1])
            
        # Criar um objeto Point com as coordenadas
        point = Point(lon, lat)
            
        # Verificar se o ponto está dentro do polígono
        if polygon.contains(point):
            coordenadas_filtradas.append((lon, lat))
            
# Agora você pode usar a lista "coordenadas_filtradas" como necessário
for coord in coordenadas_filtradas:
    print(coord)
