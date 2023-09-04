import os
import pyproj

def lat_lon_to_utm(lat, lon):
    transformer = pyproj.Transformer.from_crs('EPSG:4326', 'EPSG:32733', always_xy=True)
    utm_easting, utm_northing = transformer.transform(lon, lat)
    return utm_easting, utm_northing

# Caminho para o arquivo de coordenadas
input_file_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'coordenadasEspinhoB.txt')
output_file_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'utmcoordenadas.txt')

# Ler as coordenadas do arquivo de entrada
coordinates = []
with open(input_file_path, 'r') as input_file:
    lines = input_file.readlines()
    for line in lines:
        if line.startswith('('):
            coords_str = line.strip()[1:-1]  # Remover parênteses
            lat, lon, elev = map(float, coords_str.split(', '))
            coordinates.append((lat, lon, elev))

# Converter as coordenadas para UTM e escrever no arquivo de saída
with open(output_file_path, 'w') as output_file:
    for lat, lon, elev in coordinates:
        utm_easting, utm_northing = lat_lon_to_utm(lat, lon)
        output_file.write(f'UTM Easting: {utm_easting}, UTM Northing: {utm_northing}, Elevation: {elev}\n')

print('Coordenadas convertidas e salvas em utmcoordenadas.txt')
