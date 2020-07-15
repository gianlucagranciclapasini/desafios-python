"""
DESAFIO 3
Realizar una función separar(lista). Tiene que tomar una lista.
Tiene q devolver 2 listas ORDENADAS.
    - La primera con ciudades que superen los 100 arboles plantados.
    - La segunda con el resto.
Luego qué cantidad de ciudades han plantado más de 100 árboles.
"""

# Acá no voy a pedir datos al usuario, pero sería algo parecido como el Desafío 2 si quisiéramos implementarlo...
ciudades = {
    "Buenos Aires": 2500,
    "Resistencia": 30,
    "Corrientes Capital": 4000,
    "Posadas": 6500,
    "San Salvador de Jujuy": 10
}


def separar(datos):
    """
    Esta función recibe un diccionario como parámetro. Anexa valores mayores a una lista y menores a otra.
    Además cuenta los mayores de 100. Finalmente, imprime por pantalla
    """
    mayores = []
    menores = []
    contar_mayores = 0

    for clave, valor in datos.items():
        if valor > 100:
            mayores.append(clave)
            contar_mayores += 1
        else:
            menores.append(clave)
    
    print("Lista de ciudades que plantaron mas de 100 árboles: ", mayores)
    print("Lista de ciudades que plantaron menos de 100 árboles: ", menores)
    print("Cantidad de ciudades que plantaron mas de 100 árboles:", contar_mayores)

separar(ciudades)