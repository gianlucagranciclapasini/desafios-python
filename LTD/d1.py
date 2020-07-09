"""
Escribir un programa que pregunte a diferentes personas cuánto conocen sobre contaminación del 1 al 10, almacene estos valores en una lista y los muestre por pantalla ordenados de menor a mayor.
"""

lista = []
continuar = False
while True:
    while True:
        conocimiento = int(input('Del 1 al 10: ¿Cuánto conoces sobre contaminación ambiental?: '))
        if conocimiento < 1 or conocimiento > 10:
            print("Has ingresado un número incorrecto.")
        else:
            lista.append(conocimiento)
            break
    continuar = int(input("¿Desea agregar otro dato?\n\t1- SI\n\t2- NO\nINGRESO: "))
    if continuar == 2:
        break
print(lista)
