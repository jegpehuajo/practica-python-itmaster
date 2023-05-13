"""
Escribir un programa que permita al usuario ingresar dos números enteros. 
La computadora debe indicar si el mayor es divisible por el menor.
(Un número entero a es divisible por un número entero b 
cuando el resto de la división entre a y b es 0)
"""

n1 = int(input("Escribir un nro: "))
n2 = int(input("Escribir un nro: "))

if (n1 >= n2) and (n1 % n2) == 0:
  print(f"El numero {n1} es mayor a {n2} y son divisibles.")
elif n2 % n1 == 0:
  print(f"El numero {n2} es mayor a {n1} y es divisible por {n1}")
else:
   print(f"No es divisible el numero {n1} por el {n2}")
    

