hectarea = float(input("Ingrese cuanto mide el terreno: "))
suelo = input("Ingrese el tipo de suelo (1- MATORRAL 2- OTRO): ")
comp = float(input("Ingrese la cantidad de compuesto que existe: "))

porcentaje = hectarea * comp / 100

if porcentaje < 10 and suelo != 1:
    print("No es factible")
else:
    print("Es factible")
