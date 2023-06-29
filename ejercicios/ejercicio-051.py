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

def numero_minimo(numeros):
    min = numeros[0]
    for n in numeros:
        if n < min:
            min = n
    return min

while numero != 0:
    numero = int(input("Ingrese un numero: "))
    if numero != 0:
        numeros.append(numero)

print("La lista completa de numeros es: ",numeros)
print("El numero maximo es: ",int(numero_maximo(numeros)))
print("El numero minimo es: ",int(numero_minimo(numeros)))
