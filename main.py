# from menu_inicial import MenuInicial
from baseDeDatos import baseDatos
from usuario import Usuario

# menuInicial = MenuInicial()
# resultadoMenu = menuInicial.menu()

# INSTANCIANDO USUARIOS 
cantidadDeUsuarios = len(baseDatos.selectTodoUsuario())
for x in range(cantidadDeUsuarios):
    globals() [f"usuario{x}"] = Usuario(*(baseDatos.selectTodoUsuario()[x]))

# print('\n\n--------DATOS DE USUARIO----------')
# print(f'\nNOMBRE: {globals()[f"usuario{cantidadDeUsuarios-1}"].get_nombre()}')
# print(f'APELLIDO: {globals()[f"usuario{cantidadDeUsuarios-1}"].get_apellido()}')
# print(f"{globals()[f'usuario{cantidadDeUsuarios-1}'].get_id()}")

globals()[f'usuario{cantidadDeUsuarios-1}'].menuUsuarioInicial()
