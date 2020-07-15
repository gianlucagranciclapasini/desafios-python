"""
Realiza una función llamada relacion(a, b) que a partir de toneladas recicladas de dos ciudades se cumpla lo siguiente:
Si el primer número es mayor que el segundo, debe devolver el nombre de la ciudad 1.
Si el primer número es menor que el segundo, debe devolver el nombre de la ciudad 2.
Si ambos números son iguales, debe devolver el nombre de ambas.
"""

def relacion(datos):
    """
    Esta funcion recibe un diccionario con dos elementos como parámetro.
    Luego toma los valores mas altos que haya con la funcion max().
    Luego retorna la clave q corresponda a ese valor alto.
    """
    mas_alto = max(datos.values())
    # En este caso usamos una list comprehension para escribir menos codigo.
    # En definitiva retorna clave.
    return ([clave for clave, valor in ciudades.items() if valor == mas_alto])


# Pido datos al usuario, en este caso 2 veces
# Ademas valido q no se repita ninguna key con while.
ciudades = {}

for i in range(2):
    while True:
        nombre_ciudad = input('Ingresa el nombre de la ciudad: ')
        if nombre_ciudad in ciudades:
            print("Ya existe ese nombre. Reintentar")
        else:
            break
    ton_basura = float(input('Ingresa las toneladas de basura que se producen: '))
    ciudades[nombre_ciudad] = ton_basura

# Como lo que retorna la funcion es una lista, la pasamos a string y separamos con coma con la función join.
print(", ".join(relacion(ciudades)))