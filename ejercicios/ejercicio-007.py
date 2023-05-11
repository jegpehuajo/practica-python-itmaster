"""
Escribir un programa que permita ingresar un número entero. 
Debe mostrarse el número ingresado:
    a. Multiplicado por 10. (utilizar el operador *)
    b. Dividido por 10. (utilizar el operador /)
    c. Elevado al cuadrado. (utilizar el operador **)
"""
N = 10
n = int(input("Ingrese un numero: "))
m = n * N
d = n / N
e = n ** 2
print(f"El numero {n} multiplicado por {N} da: {m}")
print(f"El numero {n} dividido por {N} da: {d}")
print(f"El numero {n} elevado al cuadrado da: {e}")
