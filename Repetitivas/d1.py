"""
Nos han pedido desarrollar una aplicación móvil para reducir comportamientos inadecuados para el ambiente.
a) Te toca escribir un programa que simule el proceso de Login. 
Para ello el programa debe preguntar al usuario la contraseña, 
y no le permita continuar hasta que la haya ingresado correctamente.
b) Modificar el programa anterior para que solamente permita una cantidad fijade intentos.
"""

i = 0

uname = input("Ingresa el nombre de usuario: ")
while i < 3:
	contra = input("Ingresa la contraseña: ")
	if contra != "INFO2020":
		print("INCORRECTO")
	else:
		break
	i += 1

if i == 3:
	print("Intentos agotados.")
else:
	print("Login correcto\nBienvenido",uname)