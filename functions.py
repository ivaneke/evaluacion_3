import random, time, os

def limpiar():
    os.system("cls")

def menu_principal():
    print("MENÚ PRINCIPAL\n")
    print(" 1. Grabar\n 2. Buscar\n 3. Imprimir certificados\n 4. Salir\n")

def obtener_nif():
    numero_nif = str(input("Ingrese número de NIF: "))
    while len(numero_nif) > 8:
        numero_nif= str(input("Ingrese NIF con el formato correcto (Máximo 8 dígitos): "))
    agregar_ceros = 8 - len(numero_nif)
    numero_nif = "0" * agregar_ceros + numero_nif

    bandera_ciudad = True
    while bandera_ciudad:
        ciudad = str(input("Ingrese ciudad de residencia. Madrid - Barcelona - Sevilla: ")).upper()
        if ciudad == "MADRID":
            codigo_ciudad = "MAD"
            bandera_ciudad = False
        elif ciudad == "BARCELONA":
            codigo_ciudad = "BAR"
            bandera_ciudad = False
        elif ciudad == "SEVILLA":
            codigo_ciudad = "SEV"
            bandera_ciudad = False
        if bandera_ciudad == True:
            print("Ciudad no válida")
    nif= numero_nif + "-" + codigo_ciudad  
    return nif

def obtener_nombre():
    nombre=input("Ingrese nombre:\n")
    while len(nombre)<8:
        nombre=input("Ingrese nombre (mínimo 8 caracteres):\n")
    return nombre

def obtener_nacionalidad():
    nacionalidad=input("Ingrese nacionalidad:\n")
    while nacionalidad == "":
        nacionalidad=input("Campo requerido. Por favor ingrese nacionalidad:\n")
    return nacionalidad

def obtener_edad():
    while True:
        try:
            edad=int(input("Ingrese edad:\n"))
            while edad < 15:
                edad=int(input("Ingrese una edad correcta (mayor o igual a 15): "))
            break
        except:
            print("Campo edad sólo acepta valores numéricos")
    return edad 

def registrar_ciudadano(lista):
    while True:
        ciudadano = []
        nif = obtener_nif()           
        ciudadano.append(nif)
        
        nombre = obtener_nombre()
        ciudadano.append(nombre)

        nacionalidad = obtener_nacionalidad()
        ciudadano.append(nacionalidad)
        
        edad = obtener_edad()
        ciudadano.append(edad)

        fecha_nac = str(random.randint(1, 31))+'/'+str(random.randint(1, 12))+'/'+str(2024-edad)
        ciudadano.append(fecha_nac)

        opc_conyu = random.randint(1,2)
        if opc_conyu == 1:
            estado_conyugal = "Soltero"
        elif opc_conyu == 2:
            estado_conyugal = "Casado"
        ciudadano.append(estado_conyugal)

        salario = str(random.randint(1200,10000))+" euros"
        ciudadano.append(salario)

        lista.append(ciudadano)
        print("Registrado con éxito\n")
        print(ciudadano)              
        
        agregar=int(input("Desea agregar otro registro?\n 1.Sí 2.No\n"))
        while agregar != 1 and agregar != 2:
            agregar=int(input("Ingrese una opción válida\n 1.Sí 2.No\n"))
        if agregar == 1:
            continue
        elif agregar == 2:
            break

def buscar_ciudadano(lista):
    nif_buscar = input("Ingrese NIF del ciudadano:\n").upper()
    encontrado = False
    for ciudadano_buscar in lista:
        if nif_buscar==ciudadano_buscar[0]:
            print("Información del ciudadano:\n")
            print("NIF :" , ciudadano_buscar[0])
            print("NOMBRE :" , ciudadano_buscar[1])
            print("NACIONALIDAD : " , ciudadano_buscar[2])
            print("EDAD : " , ciudadano_buscar[3])
            encontrado = True
    if encontrado == False:
        print("Id no existe")


def sub_menu():
    print("Imprimir Certificados\n")
    print(" 1. Nacimiento\n 2. Estado conyugal\n 3. Salario\n 4. Salir\n")

def cert_nacimiento(lista):
    nif_buscar = input("Ingrese NIF del ciudadano:\n").upper()
    encontrado = False
    for ciudadano_buscar in lista:
        if nif_buscar==ciudadano_buscar[0]:
            print(f"""
--------------------------------------------------------------------------
                                    
                  
                    CERTIFICADO DE NACIMIENTO
                
                NIF:                   {ciudadano_buscar[0]}
                NOMBRE:                {ciudadano_buscar[1]}
                FECHA DE NACIMIENTO:   {ciudadano_buscar[4]}
                NACIONALIDAD:          {ciudadano_buscar[2]}
                EDAD:                  {ciudadano_buscar[3]}


---------------------------------------------------------------------------
            """)

            encontrado = True
    if encontrado == False:
        print("Id no existe")

def cert_conyugal(lista):
    nif_buscar = input("Ingrese NIF del ciudadano:\n").upper()
    encontrado = False
    for ciudadano_buscar in lista:
        if nif_buscar==ciudadano_buscar[0]:
            print(f"""
--------------------------------------------------------------------------
                                    
                  
                    CERTIFICADO DE ESTADO CONYUGAL
                
                ESTADO CONYUGAL:       {ciudadano_buscar[5]}
                NIF:                   {ciudadano_buscar[0]}
                NOMBRE:                {ciudadano_buscar[1]}
                NACIONALIDAD:          {ciudadano_buscar[2]}
                EDAD:                  {ciudadano_buscar[3]}


---------------------------------------------------------------------------
            """)

            encontrado = True
    if encontrado == False:
        print("Id no existe")

def cert_salario(lista):
    nif_buscar = input("Ingrese NIF del ciudadano:\n").upper()
    encontrado = False
    for ciudadano_buscar in lista:
        if nif_buscar==ciudadano_buscar[0]:
            print(f"""
--------------------------------------------------------------------------
                                    
                  
                    CERTIFICADO DE SALARIO MENSUAL
                
                SALARIO MENSUAL:       {ciudadano_buscar[6]}
                NIF:                   {ciudadano_buscar[0]}
                NOMBRE:                {ciudadano_buscar[1]}
                NACIONALIDAD:          {ciudadano_buscar[2]}
                EDAD:                  {ciudadano_buscar[3]}


---------------------------------------------------------------------------
            """)

            encontrado = True
    if encontrado == False:
        print("Id no existe")
