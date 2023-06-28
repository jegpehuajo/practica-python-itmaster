"""
Una remisería requiere un sistema que calcule el precio de un viaje a partir de la cantidad de km
que desea recorrer el usuario.

Tiene la siguiente tarifa:
    Viaje mínimo $50
    Si recorre entre 0 y 10km: $20/km
    Si recorre 10km o más: $15/km

    Escribir un programa que permita ingresar la cantidad de km que desea recorrer el usuario y 
    muestre el precio del viaje.
"""

COSTO_MINIMO = 50
PRECIO_HASTA_10KM = 20
PRECIO_DESDE_10KM = 15

cantidad_km = int(input("Ingrese cantidad de KM a recorrer: "))

if cantidad_km <= 10:
    precio = cantidad_km * PRECIO_HASTA_10KM
    if precio >= COSTO_MINIMO:
        print(f"El precio del viaje es {precio} para {cantidad_km} KM")
    else:
        print(f"El costo minimo del viaje es: {COSTO_MINIMO}")
elif cantidad_km > 10:
    precio = cantidad_km * PRECIO_DESDE_10KM
    print(f"El costo del viaje es: {precio} por {cantidad_km} KM.")  