"""
Escribir un programa que permita al usuario ingresar números hasta que se introduzca un 0.
La computadora debe mostrar el número máximo y el número mínimo.
"""
numeros = []
numero = []

print("Si ingresa 0 sale del programa.")

def numero_maximo(numeros):
    max = numeros[0]
    for n in numeros:
        if n > max:
            max = n
    return max

while numero != 0:
    numero = int(input("Ingrese un numero: "))
    if numero != 0:
        numeros.append(numero)

print(numeros)
print(int(numero_maximo(numeros)))
