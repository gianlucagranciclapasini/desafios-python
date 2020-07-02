"""
 Ingredientes comunes: Verduras y berenjena.
 Ingredientes Receta 1: Lentejas y apio.
 Ingredientes Receta 2: Morrón y Cebolla.
"""

# Definiendo ingredientes en listas
receta1 = ['Lentejas', 'Apio']
receta2 = ['Morrón', 'Cebolla']
comunes = ['Verduras', 'Berenjena']

receta = int(input("Seleccioná tu receta: "))

if receta == 1:
    print("Los ingredientes de la receta son:", " y ".join(receta1))
elif receta == 2:
    print("Los ingredientes de la receta son:", " y ".join(receta2))
else:
    print("ERROR: Opción incorrecta")

# Ahora preguntamos por el ingrediente común.
ing_comun = int(input("Seleccioná el ingrediente común\n1.- Verduras\n2.- Berenjena\n"))
