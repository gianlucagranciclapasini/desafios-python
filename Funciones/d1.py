"""
Tiempos de degradación:
	- Bolsa plástica: 150 años
	- Botella PET: 1000 años
	- Tetrabrik: 30 años
	- Chicle: 5 años
Se solicita una función para que dado el ingreso de un elemento, 
se solicite tipo: Bolsa de plástico, botella PET, 
envase tetrabrik o chicle, e imprima la cantidad 
de años que tarda en degradarse.
"""

def tiempo_degradacion(elemento):
	if elemento == "Botella":
		return "150 años"
	elif elemento == "Botella PET":
		return "1000 años"
	elif elemento == "Tetrabrik":
		return "30 años"
	elif elemento == "Chicle":
		return "5 años"
	else:
		return "Elemento incorrecto"

print(tiempo_degradacion(input("Ingrese el elemento: ")))