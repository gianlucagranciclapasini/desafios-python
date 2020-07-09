"""
Crea una tupla con los factores que más afectan a los mares. Luego para jugar con niños y niñas, aprendiendo sobre contaminación del agua crea un programa que pida números, si el numero esta entre 1 y la longitud máxima de la tupla, muestra el contenido de esa posición sino muestra un mensaje de error.

El programa termina cuando el usuario introduce un cero.
"""

factores = ("plastico", "petroleo", "desechos industriales", "metal oxidable")

while True:
    numero = int(input("Ingresa un numero: "))
    if numero >= 1 and numero <= len(factores):
        print(factores[0:numero])
    elif numero == 0:
        break
    else:
        print("Datos incorrectos")
