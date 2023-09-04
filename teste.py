import os
import geopandas as gpd
from alphashape import alphashape
from descartes import PolygonPatch
import matplotlib.pyplot as plt

data = os.path.join(os.path.expanduser('~'), 'Desktop', 'EspinhoBranco.shp')
gdf = gpd.read_file(data)

# Converter geometrias MultiLineString em LineString individuais
line_strings = gdf.explode()

# Extrair as coordenadas dos vértices das geometrias LineString
coords = [point.coords[0] for point in line_strings['geometry']]

# Gerar a alphashape
alpha_shape = alphashape(coords, alpha=0.7)

# Plotar a Alphashape com Matplotlib
fig, ax = plt.subplots(figsize=(10, 8))
ax.scatter(*zip(*coords), color='blue', label='Pontos')
patch = PolygonPatch(alpha_shape, alpha=0.2, color='green')
ax.add_patch(patch)
ax.set_aspect('equal', 'box')
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.set_title('Alphashape dos Pontos')
ax.legend()
plt.show()

# Plotar o GeoDataFrame
gdf.plot()
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Pontos do GeoDataFrame')
plt.show()
