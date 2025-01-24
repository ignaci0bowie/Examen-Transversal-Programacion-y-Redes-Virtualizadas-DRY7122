import math
import sys

def calcular_distancia(lat1, lon1, lat2, lon2):
    """
    Calcula la distancia entre dos puntos geográficos usando la fórmula de Haversine.
    Retorna la distancia en kilómetros.
    """
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    R = 6371
    return R * c

def calcular_duracion(distancia, medio_transporte):
    """
    Calcula la duración del viaje en horas dependiendo del medio de transporte.
    """
    velocidades = {
        "bus": 80,
        "barco": 40,
        "avión": 900
    }
    velocidad = velocidades.get(medio_transporte.lower(), 80)
    return distancia / velocidad

def mostrar_narrativa(origen, destino, distancia_km, duracion, medio_transporte):
    """
    Genera y muestra una narrativa descriptiva del viaje.
    """
    distancia_millas = distancia_km * 0.621371
    print("\n=== Información del viaje ===")
    print(f"Origen: {origen}")
    print(f"Destino: {destino}")
    print(f"Distancia: {distancia_km:.2f} km ({distancia_millas:.2f} millas)")
    print(f"Medio de transporte: {medio_transporte.capitalize()}")
    print(f"Duración estimada: {duracion:.2f} horas\n")
    narrativa = (
        f"Tu viaje desde {origen} hasta {destino} a bordo de un {medio_transporte.lower()} "
        f"te llevará aproximadamente {duracion:.2f} horas. Recorrerás una distancia de "
        f"{distancia_km:.2f} kilómetros, disfrutando de las vistas y paisajes "
        f"característicos que separan estas dos ciudades emblemáticas de América del Sur."
    )
    print(narrativa)

def obtener_entrada(mensaje):
    """
    Solicita entrada al usuario y permite salir escribiendo 's'.
    """
    entrada = input(mensaje).strip().lower()
    if entrada == "s":
        print("¡Has salido del programa!")
        sys.exit()
    return entrada

# Coordenadas de ciudades
ciudades = {
    "santiago de chile": (-33.4489, -70.6693),
    "la plata de argentina": (-34.9215, -57.9545)
}

# Solicitar entrada al usuario
origen = obtener_entrada("Ingrese la Ciudad de Origen (o 's' para salir): ")
destino = obtener_entrada("Ingrese la Ciudad de Destino (o 's' para salir): ")

if origen in ciudades and destino in ciudades:
    lat1, lon1 = ciudades[origen]
    lat2, lon2 = ciudades[destino]
    distancia_km = calcular_distancia(lat1, lon1, lat2, lon2)
    print("\nOpciones de transporte: Bus, Barco, Avión")
    medio_transporte = obtener_entrada("Ingrese el medio de transporte (o 's' para salir): ")
    duracion = calcular_duracion(distancia_km, medio_transporte)
    mostrar_narrativa(origen.capitalize(), destino.capitalize(), distancia_km, duracion, medio_transporte)
else:
    print("\nError: Una o ambas ciudades no se encuentran en la base de datos.")
