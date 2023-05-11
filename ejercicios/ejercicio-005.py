"""
Escribir un programa que solicite al usuario ingresar dos notas de un alumno.
El programa debe mostrar por pantalla el promedio de las notas de la siguiente manera: 
"Notas: [nota1] , [nota2] ==> promedio: [(nota1+nota2)/2]".
Ejemplo: Si el usuario ingresa 7 y 8, el programa debe mostrar por pantalla: "Notas: 7 , 8 ==> promedio: 7.5".
n1 = int(input("Ingrese una nota: "))
n2 = int(input("Ingrese una nota: "))

promedio = (n1+n2)/2

print(f"Notas: {n1}, {n2} ==> promedio: {promedio}.")
