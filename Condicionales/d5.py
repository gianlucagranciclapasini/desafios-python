"""
La sección A esta formada por los barrios céntricos cuyo nombre comienza con una letra anterior a M 
y los barrios no céntricos con nombre posterior a la M, y la sección B el resto.
"""
nom_barrio = input("Ingresa el nombre del barrio: ")
# Convierto la primera letra a mayuscula.
nom_barrio = nom_barrio.capitalize()
ubicacion = int(input("Selecciona la ubicación:\n\t1.- CENTRICO\n\t2.- NO CENTRICO\nINGRESO: "))

# Validación de la ubicación
if ubicacion != 1 and ubicacion != 2:
	print("Ubicación incorrecta.")
else:
	# Con el método ord() recibo un caracter (en este caso el primero del nombre) y obtengo su valor UNICODE.
	# Por este motivo convertí a mayúscula el primer caracter, porque C y c no tienen el mismo valor UNICODE.
	if ubicacion == 1 and ord(nom_barrio[0]) < 77 or ubicacion == 2 and ord(nom_barrio[0]) > 77:
		print("Pertenece a la sección A")
	else:
		print("Pertenece a la sección B")