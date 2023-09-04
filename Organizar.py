import os
# Caminho para o arquivo com as outras coordenadas
input_file_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'Outras_coordenadas.txt')

# Caminho para o novo arquivo com as coordenadas no formato desejado
output_file_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'Outras_coordenadas_modified.txt')

# Modificar o arquivo com as outras coordenadas
with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
    for line in input_file:
        coords = line.strip().split(' ')
        formatted_coords = ' '.join([f'({coords[i]} {coords[i+1]})' for i in range(0, len(coords), 2)])
        output_file.write(formatted_coords + '\n')

print("Arquivo modificado criado com sucesso!")
