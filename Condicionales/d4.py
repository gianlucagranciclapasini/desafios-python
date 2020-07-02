"""
 Ingredientes comunes: Verduras y berenjena.
 Ingredientes Receta 1: Lentejas y apio.
 Ingredientes Receta 2: Morrón y Cebolla.
"""

# Definiendo ingredientes en listas
receta1 = ['Lentejas', 'Apio']
receta2 = ['Morrón', 'Cebolla']
comunes = ['Verduras', 'Cebolla']

# Mostrando por pantalla las listas. El formato de salida sale como string con el metodo join
print("1.-",", ".join(receta1))
print("2.-",", ".join(receta2))
rel = int(input("Selecciona tu receta: "))

ex = int(input("Selecciona un ingrediente común: "))

if rel > 2 or ex > 2:
    print("Ingreso de datos incorrecto: ")
else:
    print("Su receta elegida es: ",

#print("1.-", comunes[0],"\n2.-", comunes[1]
