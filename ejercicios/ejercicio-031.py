"""
Una editorial determina el precio de un libro según la cantidad de páginas que contiene. 
El costo básico del libro es de 1000,más35,10 por página con encuadernación rústica. 
Si el número de páginas supera las 300 la encuadernación debe ser especial, 
lo que incrementa el costo en 1200.
Además,si el número de páginas sobrepasa las 600 se hace necesario otro procedimiento 
de encuadernación que incrementa el costo en 880. 
Desarrollar un programa que calcule el costo de un libro dado el número de páginas.
"""

COSTO_BASICO = 1000
PLUS = 35
COSTO_PAGINA = 10
ENCUADERNACION_ESPECIAL = 1200
PROCEDIMIENTO_ENCUADERNACION = 880

numero_paginas = int(input("Ingrese el numero de paginas que tiene el libro: "))

if numero_paginas <= 300 and numero_paginas > 0:
    total = COSTO_BASICO + PLUS + (numero_paginas * COSTO_PAGINA)
    print(f"El costo total del libro es: {total} y la encuadernación es rustica.")
elif numero_paginas > 300 and numero_paginas <= 600:
    total = COSTO_BASICO + PLUS + (numero_paginas * COSTO_PAGINA) + ENCUADERNACION_ESPECIAL
    print(f"El costo total del libro es: {total} y la encuadernación especial cuesta: {ENCUADERNACION_ESPECIAL}")
elif numero_paginas > 600:
    total = COSTO_BASICO + PLUS + (numero_paginas * COSTO_PAGINA) + ENCUADERNACION_ESPECIAL + PROCEDIMIENTO_ENCUADERNACION
    print(f"El costo total del libro es: {total} y tiene encuadernación especial y un procedimiento de encuadernación.")
else:
    print("El numero de paginas no es correcto.")