import os

# Caminho para o arquivo coordenadasEspinhoB.txt
coordinates_file_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'coordenadasEspinhoB.txt')

# Criar uma pasta para salvar os arquivos
output_folder = os.path.join(os.path.expanduser('~'), 'Desktop', 'CoordenadasSeparadas')
os.makedirs(output_folder, exist_ok=True)

# Processar o arquivo de coordenadas
with open(coordinates_file_path, 'r') as coordinates_file:
    elevation_coords_x = {}
    elevation_coords_y = {}
    current_elevation = None
    for line in coordinates_file:
        if line.startswith("Elevation:"):
            current_elevation = float(line.split(':')[1].strip())
            elevation_coords_x[current_elevation] = []
            elevation_coords_y[current_elevation] = []
        else:
            coords = line.strip('()\n').split(', ')
            if len(coords) == 3:  # Verificar se há três valores (lon, lat, elevation)
                lon = float(coords[0])
                lat = float(coords[1])
                elevation_coords_x[current_elevation].append(lon)
                elevation_coords_y[current_elevation].append(lat)

# Função para salvar coordenadas em arquivo
def salvar_coordenadas(nome_arquivo, coords_list):
    with open(nome_arquivo, 'w') as arquivo:
        for coord in coords_list:
            coord_str = str(coord).replace('.', ',')  # Substituir pontos por vírgulas
            arquivo.write("{}\n".format(coord_str))

# Salvar coordenadas x e y agrupadas por elevação em arquivos separados
for elevation, coords_x in elevation_coords_x.items():
    x_file_path = os.path.join(output_folder, f'coordenadas_x_{elevation}.txt')
    salvar_coordenadas(x_file_path, coords_x)

for elevation, coords_y in elevation_coords_y.items():
    y_file_path = os.path.join(output_folder, f'coordenadas_y_{elevation}.txt')
    salvar_coordenadas(y_file_path, coords_y)

print("Arquivos salvos com sucesso!")
