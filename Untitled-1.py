import pyproj
from shapely.geometry import Polygon
from shapely.ops import transform

def calculate_area(coords):
    polygon = Polygon(coords)
    projected_polygon = transform(
        pyproj.Transformer.from_crs('EPSG:4326', 'EPSG:32733', always_xy=True).transform,
        polygon
    )
    area = projected_polygon.area
    return area

# Coordenadas do polígono
coords = [
    (-37.30075337599988, -7.064166666666672),
    (-37.30097222222224, -7.064208736296802),
    (-37.30086279911106, -7.064187701481737),
]

# Calcular a área em metros quadrados
area = calculate_area(coords)
print(f'Área do polígono: {area:.10f} metros quadrados')
