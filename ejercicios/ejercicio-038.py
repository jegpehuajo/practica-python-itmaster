"""
Escribir un programa que permita ingresar un número entero n. 
Debe mostrar los primeros 10 múltiplos de n.
"""

CANTIDAD = 10

valor = int(input(f"Ingrese un numero entero para mostrar los primeros {CANTIDAD} multiplos: "))

print("********************")

for v in range(1, CANTIDAD + 1):
    multiplo = valor * v
    print(f"{valor} X {v} = {multiplo}")

print("********************")