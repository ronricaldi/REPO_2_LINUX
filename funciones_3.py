
# ADMINISTADOR
# nombre = adminron
# password = aviador

# USUARIO_1
# nombre = juan
# password = juan1234

def login_3 ():
    print("""
          **********************************
          Bienvenido al sistema MAESMASTORE"
          **********************************
          """)
    nombre = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su password: ")
    
    if nombre == "adminron" and password == "aviador":
        return "administrador"
    elif nombre == "juan" and password == "juan1234":
        return "usuario"
    else:
        return "Datos incorrectos"
    