
def menu_administrador_3():
    while True:
        print("""
              ***************************************
              Bienvenido al sistema de administrador
              **************************************
              """)
        print("(1) Crear un nuevo usuario")
        print("(2) Eliminar un usuario")
        print("(3) Salir del sistema de administrador")
        opcion = int(input("Ingrese la accion requerida: "))
        if opcion == 1:
            print("Creación de un USUARIO en proceso >>>>>>>")
        elif opcion == 2:
            print("Ingrese el nombre del usuario que desea eliminar: ")
        elif opcion == 3:
            print("Usted está saliendo del sistema de administrador >>>>>")
        else:
            print("Opción incorrecta")