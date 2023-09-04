import os

# Caminhos para os arquivos
coordinates_file_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'coordinates_above_260.txt')
outras_coordenadas_file_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'Outras_coordenadas_modified.txt')

# Coordenadas das áreas a serem mantidas
coordenadas_mantidas = set()

# Ler as coordenadas do arquivo "outras_coordenadas"
with open(outras_coordenadas_file_path, 'r') as outras_coordenadas_file:
    line = outras_coordenadas_file.readline()
    coord_groups = line.strip().split('), ')
    for coord_group in coord_groups:
        lon, lat = map(float, coord_group.strip('()').split(', '))
        coordenadas_mantidas.add((lon, lat))

# Filtrar as coordenadas do arquivo "coordinates_above_260"
coordenadas_filtradas = []

with open(coordinates_file_path, 'r') as coordinates_file:
    lines = coordinates_file.readlines()

elevation = None
for line in lines:
    if line.startswith("Elevation:"):
        elevation = float(line.split(':')[1].strip())
    else:
        coords = line.strip('()\n').split(', ')
        lon, lat = map(float, coords[0].split())
        if (lon, lat) in coordenadas_mantidas:
            coordenadas_filtradas.append((lon, lat, elevation))

# Agora você pode usar a lista "coordenadas_filtradas" como necessário
for coord in coordenadas_filtradas:
    print(coord)
