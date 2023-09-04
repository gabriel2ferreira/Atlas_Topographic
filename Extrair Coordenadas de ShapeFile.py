import os
import geopandas as gpd

# Caminho shapefile
shapefile_path = "C:/Users/Gabriel de Lima/DIO/Atlas_Topographic/Espinho.shp"

# Carregando o shapefile
gdf = gpd.read_file(shapefile_path)

# Dicionário para armazenar as coordenadas por elevação
elevation_coordinates = {}

# Iterando sobre as geometrias das curvas de nível
for index, row in gdf.iterrows():
    elevation = row['ELEV']  # 'ELEV' contém informações de elevação
    coordinates = row['geometry'].coords
    if elevation not in elevation_coordinates:
        elevation_coordinates[elevation] = []
    elevation_coordinates[elevation].extend(coordinates)

# Caminho para o arquivo de bloco de notas
output_file_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'coordinates_by_elevation.txt')

# Escrevendo as coordenadas organizadas no arquivo de bloco de notas
with open(output_file_path, 'w') as output_file:
    for elevation, coords in elevation_coordinates.items():
        output_file.write(f"Elevation: {elevation}\n")
        for coord in coords:
            output_file.write(f"{coord}\n")
        output_file.write("\n")

print(f"Coordenadas organizadas foram salvas em: {output_file_path}")


#// 
