#Escriba un programa que permita imprimir un tablero Ecológico (verde y blanco) de
#acuerdo al tamaño indicado. Por ejemplo el gráfico a la izquierda es el resultado de un
#tamaño: 8x6
filas = int(input("Ingrese la cantidad de filas: "))
columnas = int(input("Ingrese la cantidad de columnas: "))

# Utilizamos bucles for anidados
# Con esto por ejemplo el valor de x se mantiene
# Cambia recién cuando "y" termina de iterar, dependiendo de cuanto vale el parametro range
# Cuando termina una iteración, osea sale del bucle for anidado, imprime un salto de linea
# el end en este caso es para eliminar el espaciado q queda con el salto solo.

for x in range(filas):
    for y in range(columnas):
        # Obtenemos el valor del módulo de la suma de el numero de iteracion "x" mas el de "y"
        # Si es 0 imprime la letra "B" de blanco y con end inserta un espacio.
        if (x + y) % 2 == 0:
            print("B", end=" ")
        else:
            print("V", end=" ")
    print("\n",end="")

"""
B V B V B   --> Acá x = 0 e y = 4 al final 
V B V B V   --> Acá x = 1 e y = 4 al final
B V B v B   --> Acá x = 2 e y = 4 al final
"""
