"""
Desafío 4
Escribir un programa que cargue una tupla con nombres 
de especie, y para cada nombre de especie imprima 
el mensaje Hola soy ......, cuidame.

Modificá el programa anterior y dada una posición 
inicial p y una cantidad n, imprima el mensaje 
anterior para los n nombres que se encuentran a 
partir de la posición p (i).
"""

nombres = ("Perro", "Gato", "Gallina", "Caballo", "Carpincho")

inicio = int(input("Ingresa una posicion inicial: "))
tope = int(input("Ingresa la posicion final: "))

if inicio < 0 or tope > 5:
	print("Error. Valores incorrectos.")
else:
	for x in nombres[inicio:tope]:
		print("Hola soy "+x+", cuidame")

#print(nombres[inicio:cantidad])