
from administrador_3 import menu_administrador_3
from usuario_3 import menu_usuario_3
from funciones_3 import login_3

def menu_inicial():
    tipo_cuenta_3 = login_3()
    if tipo_cuenta_3 == "administrador":
        menu_administrador_3()
    elif tipo_cuenta_3 == "usuario":
        menu_usuario_3()
    else:
        print("Algo salió mal")
menu_inicial()
