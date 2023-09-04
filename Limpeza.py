import os

# Caminhos para os arquivos
outras_coordenadas_file_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'Outras_coordenadas.txt')
coordinates_above_260_file_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'coordinates_above_260.txt')
coordinates_above_file_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'coordinates_above.txt')

# Modificar o formato das coordenadas no arquivo "outras_coordenadas.txt"
coordenadas_modificadas = []
with open(outras_coordenadas_file_path, 'r') as outras_coordenadas_file:
    coords_group = outras_coordenadas_file.readline().strip().split(', ')
    for coord_group in coords_group:
        coords = coord_group.split(' ')
        coordenadas_modificadas.append(f"({', '.join(coords)}, -1.7976931348623157e+308)")

# Escrever as coordenadas modificadas no arquivo "coordinates_above.txt"
with open(coordinates_above_file_path, 'w') as coordinates_above_file:
    for coord in coordenadas_modificadas:
        coordinates_above_file.write(coord + '\n')

# Criar o arquivo "coordinates_above" a partir do "coordinates_above_260"
with open(coordinates_above_260_file_path, 'r') as coordinates_above_260_file:
    lines = coordinates_above_260_file.readlines()

# Remover os números depois da segunda vírgula e escrever no novo arquivo
with open(coordinates_above_file_path, 'w') as coordinates_above_file:
    coordinates_above_file.writelines(lines)

print("Arquivo 'coordinates_above' criado com sucesso!")
