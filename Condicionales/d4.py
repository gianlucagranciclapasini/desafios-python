"""
 Ingredientes comunes: Verduras y berenjena.
 Ingredientes Receta 1: Lentejas y apio.
 Ingredientes Receta 2: Morrón y Cebolla.
"""

receta = int(input("Selecciona la receta que querés:\n\t1.- Receta 1\n\t2.- Receta 2\nINGRESO: "))
if receta == 1:
	print("Los ingredientes de esta receta son:\n\t1.- LENTEJAS\n\t2.- APIO")
	ingrediente = int(input("Selecciona un ingrediente: "))
	if ingrediente != 1 and ingrediente != 2:
		print("ERROR")
	else:
		print("La receta elegida es la RECETA 1. Los ingredientes son: Verduras, Berenjena y ", end="")
		if ingrediente == 1:
			print("Lentejas")
		else:
			print("Apio")
elif receta == 2:
	print("Los ingredientes de esta receta son:\n\t1.- MORRÓN\n\t2.- CEBOLLA")
	ingrediente = int(input("Selecciona un ingrediente: "))
	if ingrediente != 1 and ingrediente != 2:
		print("ERROR")
	else:
		print("La receta elegida es la RECETA 1. Los ingredientes son: Verduras, Berenjena y ", end="")
		if ingrediente == 1:
			print("Morrón")
		else:
			print("Cebolla")
else:
	print("ERROR")