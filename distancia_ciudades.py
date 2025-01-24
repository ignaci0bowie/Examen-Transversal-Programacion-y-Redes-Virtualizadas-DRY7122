import math

def calcular_distancia(lat1, lon1, lat2, lon2):
    """
    Calcula la distancia entre dos puntos geográficos usando la fórmula de Haversine.

    Parámetros:
        lat1, lon1: Latitud y longitud del primer punto (en grados).
        lat2, lon2: Latitud y longitud del segundo punto (en grados).
    
    Retorna:
        La distancia entre los puntos en kilómetros.
    """
    # Convertir de grados a radianes
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # Diferencias de latitud y longitud
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Fórmula de Haversine
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Radio de la Tierra en kilómetros
    R = 6371
    distancia = R * c

    return distancia

# Coordenadas de Santiago de Chile y La Plata, Argentina
lat_santiago = -33.4489
lon_santiago = -70.6693
lat_la_plata = -34.9215
lon_la_plata = -57.9545

# Calcular la distancia
distancia_km = calcular_distancia(lat_santiago, lon_santiago, lat_la_plata, lon_la_plata)
print(f"La distancia entre Santiago de Chile y La Plata, Argentina, es de aproximadamente {distancia_km:.2f} km.")
