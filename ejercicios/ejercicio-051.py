"""
Escribir un programa que permita al usuario ingresar números hasta que se introduzca un 0.
La computadora debe mostrar el número máximo y el número mínimo.
"""
numeros = []
numero = []

print("Si ingresa 0 sale del programa.")

while numero != 0:
    numero = int(input("Ingrese un numero: "))
    if numero != 0:
        numeros.append(numero)
print(numeros)

