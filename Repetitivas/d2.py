# Cantidad de colillas x persona
# Porcentaje q encontro menos de 100
# Porcentaje q encontro mas de 100
# Porcentaje q encontro menos de 200
# Porcentaje q encontro mas de 200

cont_persona = 0
menos_100 = 0
mas_100 = 0
mas_200 = 0

while True:
	cantidad = int(input("Ingresa la cantidad de colillas recolectadas: "))
	cont_persona += 1
	if cantidad < 100:
		menos_100 += 1
	elif cantidad > 100 and cantidad < 200:
		mas_100 += 1
	else:
		mas_200 += 1

	seguir = int(input("¿Desea ingresar otro dato?\n\t1- SI\n\t2- NO\nINGRESO: "))
	if seguir == 1:
		continue
	else:
		break

print("Porcentaje de personas que encontró menos de 100 colillas es:", menos_100 * cont_persona / 100,"%")
print("Porcentaje de personas que encontró menos de 200 colillas es:", mas_100 * cont_persona / 100,"%")
print("Porcentaje de personas que encontró mas de 200 colillas es:", mas_200 * cont_persona / 100,"%")
