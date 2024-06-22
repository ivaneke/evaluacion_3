from functions import *
limpiar()
registro_ciudadanos = []
while True:
    try:
        menu_principal()
        opc=int(input("Escoja una opción: "))
        while opc <1 or opc > 4:
            opc=int(input("Por favor ingrese una opción entre 1 y 4: "))
        if opc==1:
            limpiar()
            print("Grabar\n")
            registrar_ciudadano(registro_ciudadanos)
        elif opc==2:
            limpiar()
            print("Búsqueda\n")
            buscar_ciudadano(registro_ciudadanos)
            x=input("Presione enter para continuar")
        elif opc==3:
            limpiar()
            while True:
                try:
                    sub_menu()
                    opc2=int(input("Escoja una opción: "))
                    while opc2 <1 or opc2 > 4:
                        opc2=int(input("Por favor ingrese una opción entre 1 y 4: "))
                    if opc2==1:
                        limpiar()
                        cert_nacimiento(registro_ciudadanos)
                    elif opc2==2:
                        limpiar()
                        cert_conyugal(registro_ciudadanos)
                    elif opc2==3:
                        limpiar()
                        cert_salario(registro_ciudadanos)
                    elif opc2==4:
                        limpiar()
                        print ("Salir")
                        opc2_salir=input("desea salir 1. Sí 2. No\n")
                        while opc2_salir!="1" and opc2_salir!="2":
                            opc2_salir=input("¿Desea volver al menú principal? 1.Sí 2.No\n")
                        if opc2_salir=="1":
                            break
                        elif opc2_salir=="2":
                            x=input("Presione Enter para volver al menú")
                except:
                    print("Opción no válida, elija entre 1 y 4")

        elif opc==4:
            limpiar()
            print ("Salir")
            opc_salir=input("desea salir 1. Sí 2. No\n")
            while opc_salir!="1" and opc_salir!="2":
                opc_salir=input("¿Desea salir? 1.Sí 2.No\n")
            if opc_salir=="1":
                break
            elif opc_salir=="2":
                x=input("Presione Enter para volver al menú")
    except:
        print("Opción no válida, elija entre 1 y 4")