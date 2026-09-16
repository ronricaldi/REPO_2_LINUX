
def menu_usuario_3():
    while True:
        print("""
              *************************************
              Bienvenido al sistema usuario MAESMA
              *************************************
              """)
        print("(1) Venta de un producto")
        print("(2) Aumentar producto a inventario")
        print("(3) Salir del sistema")
        opcion = int(input("Ingrese la opcion requerida: "))
        if opcion == 1:
            print("Ingrese el codigo del producto a vender: ")
        elif opcion == 2:
            print("Ingrese el codigo de producto a aumentar en inventario")
        elif opcion == 3:
            print("Usted está saliendo del sistema de usuario")
            
        