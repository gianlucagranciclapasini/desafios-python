"""
Crea un diccionario donde la clave sea el nombre de biólogos y el valor sea el email (no es necesario validar). Tendrás que ir pidiendo contactos hasta el usuario diga que no quiere insertar mas. No se podrán insertar nombres repetidos.
"""

diccionario = {}

while True:

    while True:
        nombre = input("Ingresa el nombre: ")
        nombre = nombre.capitalize()
        email = input("Ingresa el correo: ")
        if nombre in diccionario:
            print("Repetido")
        else:
            diccionario[nombre] = email
            break

    opt = int(input("Desea ingresar otro contacto?\n\t1- SI\n\t2- NO\nINGRESO: "))
    if opt == 2:
        break
print(diccionario)
