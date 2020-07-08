# INICIALIZO CONTADORES
cant_obs = 0
tiro_bas = 0
multado = 0

# CHECKEO QUE EL USUARIO QUIERA INGRESAR DATOS
while True:
    check = int(input("Desea ingesar datos?\n\t1- SI\n\t2- NO\nINGRESO: "))
    if check == 2:
        print("Cuenta finalizada\n")
        break
    else:
        # CUENTO LOS COCHES
        cant_obs += 1 
        # VALIDO LAS LETRAS
        while True:
            letras = input("Ingrese las 3 letras: ")
            if not letras.isalpha():
                print("No ha ingresado letras")
            else:
                break
        # VALIDO LOS NUMEROS
        while True:
            nums = input("Ingrese los 5 numeros: ")
            if not nums.isalnum():
                print("No ha ingresado numeros.")
            elif len(nums) > 5:
                print("Longitud incorrecta. Deben ser 5 numeros.")
            else:
                if "1" in nums[3]:
                    tiro_bas += 1
                if "1" in nums[4]:
                    multado += 1
                break

# SACO EL PORCENTAJE
porc = (tiro_bas + multado) * cant_obs / 100

print("//ESTADÍSTICAS//\n")
print("Cantidad de coches observados:", cant_obs)
print("Cantidad de vehículos que arrojaron basura: ", tiro_bas)
print("Porcentaje de vehículos que tiraron basura y fueron multados", porc)
