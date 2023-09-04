import numpy as np
from scipy.integrate import quad

def curva_de_nivel_area(pontos, latitude_media):
    def integrand(x):
        return np.interp(x, x_coords, y_coords)
    
    x_coords = [p[0] for p in pontos]
    y_coords = [p[1] for p in pontos]
    
    x_min = min(x_coords)
    x_max = max(x_coords)
    
    area_degrees, _ = quad(integrand, x_min, x_max)
    
    # Conversão de graus quadrados para metros quadrados
    earth_circumference = 40008000  # Circunferência média da Terra em metros
    degrees_to_meters = earth_circumference / 360
    
    area_meters = area_degrees * degrees_to_meters * degrees_to_meters * np.cos(np.radians(latitude_media))
    
    return area_meters

# Exemplo de uso
pontos = [(-37.30075337599988, -7.064166666666672),(-37.30097222222224, -7.064208736296802),(-37.301040698575605, -7.064166666666672),(-37.30097222222224, -7.064047481450074),(-37.30075337599988, -7.064166666666672)]
latitude_media = -7.06444643  # Latitude média dos pontos em graus
area_total_meters = curva_de_nivel_area(pontos, latitude_media)
print("Área da curva de nível em metros quadrados:", area_total_meters)
