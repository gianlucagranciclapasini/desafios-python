# importe
# descuento rojo = 40%
# descuento amarillo = 25%
# descuento blando = none

while True:
	importe = float(input("Ingresa el importe: "))
	descuento = input("Código:\n\tR- Rojo\n\tA- Amarillo\n\tB- Blanco\nINGRESO: ")

	while descuento != "R" and descuento != "A" and descuento != "B":
		descuento = input("REINGRESAR\nCódigo:\n\tR- Rojo\n\tA- Amarillo\n\tB- Blanco\nINGRESO: ")

	if descuento == "R":
		total = importe - importe * 0.4
	elif descuento == "A":
		total = importe - importe * 0.25
	else:
		total = importe

	print("TOTAL:$",total)

	continuar = int(input("¿Desea continuar?\n\t1 - SI\n\t2 - NO"))
	if continuar == 1:
		continue
	else:
		break
