"""
DESAFIO 3
Realizar una función separar(lista). Tiene que tomar una lista.
Tiene q devolver 2 listas ORDENADAS.
    - La primera con ciudades que superen los 100 arboles plantados.
    - La segunda con el resto.
Luego qué cantidad de ciudades han plantado más de 100 árboles.
"""

def almacenar():
    """
    Esta funcion se encarga de pedir datos, validarlos y almacenarlos en un diccionario
    """
    datos = {}
    while True:
        nombre_ciudad = input('Ingresa el nombre de la ciudad: ')
        while True:
            if nombre_ciudad in datos:
                print("Ya existe ese nombre. Reintentar")
            else:
                break
        arboles_plantados = int(input('Ingresa la cantidad de arboles plantados: '))

        datos[nombre_ciudad] = arboles_plantados
        
        continuar = int(input("¿Deseas continuar ingresando datos?\n\t1- SI\n\t2- NO\nINGRESO: "))
        if continuar == 2:
            break
    
    return datos


