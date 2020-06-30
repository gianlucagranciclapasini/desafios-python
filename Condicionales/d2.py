"""
Dado el tamaño de un pez indique si su
organismo está contaminado. Para ello tendremos 4 opciones:

- Tamaño Normal: Mensaje "Pez en buenas condiciones"
 Tamaño por debajo de lo Normal: Mensaje "Pez con problemas de
nutrición"
 Tamaño un poco por encima de lo Normal: Mensaje "Pez con
síntomas de organismo contaminado"
 Tamaño sobredimensionado: Mensaje "Pez contaminado"

"""

tamanio = float(input("Ingrese el tamaño del pez: "))

#Supongamos que el tamanio es normal es 50 cm.

if tamanio < 50:
    print("Pez con problemas de nutrición")
elif tamanio > 50 and tamanio < 55:
    print("Pez con síntomas de organismo contaminado")
elif tamanio == 50:
    print("Pez en buenas condiciones")
else:
    print("Pez contaminado")
