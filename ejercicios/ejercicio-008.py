"""
Escribir un programa que permita ingresar el valor monetario de una hora de trabajo y 
la cantidad de horas trabajadas por día, para calcular el salario semanal de un trabajador 
que trabaja todos los días hábiles y la mitad de las horas del día hábil los sábados, 
suponiendo que todas las horas tienen el mismo valor."
"""

valor_hora = int(input("Ingrese el valor de la hora: "))
cantidad_horas_diarias = int(input("Ingrese la cantidad diaria de horas trabajadas: "))
salario_semanal = valor_hora * cantidad_horas_diarias * 5
salario_total = salario_semanal + ((cantidad_horas_diarias / 2) * valor_hora)
print(f"El salario semanal es: {salario_total}")