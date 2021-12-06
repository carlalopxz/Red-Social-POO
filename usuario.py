import base64
import stdiomask
from baseDeDatos import baseDatos
from validador import Validador
from validador_logueo import ValidadorLoguin

class Usuario():
    def __init__(self,nombre, apellido,email, celular,password, cpassword,sexo, imagenPerfil,
    imagenPortada,biografia,fechaCreacionCuenta,sentimental,ciudad):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.__celular = celular
        self.__password = password
        self.__cpassword = cpassword
        self.__sexo = sexo
        self.__imagenPerfil = imagenPerfil
        self.__imagenPortada = imagenPortada
        self.__biografia = biografia
        self.__fechaCreacionCuenta = fechaCreacionCuenta
        self.__sentimental = sentimental
        self.__ciudad = ciudad
        self.__id = self.set_id()
    
    def get_id(self):
        return self.__id
    def get_nombre(self):
        return self.__nombre
    def get_apellido(self):
        return self.__apellido
    def get_email(self):
        return self.__email
    def get_password(self):
        return self.__password 
    def get_sexo(self):
        return self.__sexo
    def get_imagenPerfil(self):
        return self.__imagenPerfil
    def get_imagenPortada(self):
        return self.__imagenPortada
    def get_biografia(self):
        return self.__biografia
    def get_celular(self):
        return self.__celular
    def get_fechaCreacionCuenta(self):
        return self.__fechaCreacionCuenta
    def get_ciudad(self):
        return self.__ciudad
    def get_sentimental(self):
        return self.__sentimental
    def get_cpassword(self):
        return self.__cpassword
    
    def set_id(self):
        return baseDatos.selectIDUsuarioAct(f"'{self.get_nombre()}'")
    def set_nombre(self,nombre):
        self.__nombre = nombre
    def set_apellido(self,apellido):
        self.__apellido = apellido
    def set_email(self,email):
        self.__email = email
    def set_password(self,password):
        self.__password = password
    def set_sexo(self,sexo):
        self.__sexo = sexo
    def set_imagenPerfil(self,imagenPerfil):
        self.__imagenPerfil = imagenPerfil
    def set_imagenPortada(self,imagenPortada):
        self.__imagenPortada = imagenPortada
    def set_biografia(self,biografia):
        self.__biografia = biografia
    def set_celular(self,celular):
        self.__celular = celular
    def set_fechaCreacionCuenta(self,fechaNueva):
        self.__fechaCreacionCuenta = fechaNueva
    def set_ciudad(self,ciudad):
        self.__ciudad = ciudad
    def set_sentimental(self,sentimental):
        self.__sentimental = sentimental

    def menuUsuarioInicial(self):
        print('\nMENU USUARIO')
        while True:
            opcion = (input('''\nSeleccione una opcion:
            A) Modificar usuario
            B) Dar de baja
            C) Agregar amigo
            D) Eliminar amigo
            E) Listado de amigos
            F) SALIR!
            Opcion:  ''').lower()).strip()
            if opcion == 'a':
                self.menuUsuarioModificar()
            elif opcion == 'b':
                self.menuBaja()
            elif opcion == 'c':
                self.agregarAmigo()
            elif opcion == 'd':
                self.eliminarAmigo()
            elif opcion == 'e':
                self.listadoAmigos()
            elif opcion == 'f':
                print('Hasta pronto!')
                break
   
    #MODIFICACION DE DATOS
    def menuUsuarioModificar(self):
        while True:
            opcion = (input('''\nSeleccione una opcion a modificar:
            A) Nombre
            B) Apellido
            C) Email
            D) Celular
            E) Contraseña
            F) Sexo
            G) Imagen de Perfil
            H) Imagen de Portada
            I) Biografía
            J) Situación sentimental
            K) Ciudad
            M) SALIR!
            Opcion:  ''').lower()).strip()

            if opcion == 'a':
                self.modificarNombre()
            elif opcion == 'b':
                self.modificarApellido()
            elif opcion == 'c':
                self.modificarEmail()
            elif opcion == 'd':
                self.modificarCelular()
            elif opcion == 'e':
                self.modificarPassword()
            elif opcion == 'f':
                self.modificarSexo()
            elif opcion == 'g':
                self.modificarFotoPerfil()
            elif opcion == 'h':
                self.modificarFotoPortada()
            elif opcion == 'i':
                self.modificarBiografia()
            elif opcion == 'j':
                self.modificarSentimental()
            elif opcion == 'k':
                self.modificarCiudad()
            elif opcion == 'm':
                print('\n\nHasta pronto!')
                break
            else:
                print('Opcion equivocada, intenta nuevamente!')
    
    def modificarNombre(self):
        formularioMod = {}
        while True:
            formularioMod['nombre'] = (input('Ingrese su nombre nuevo:  ')).strip()
            formularioMod['email'] = (input('Ingrese su correo electronico:  ')).strip()
            formularioMod['password'] = (stdiomask.getpass(prompt="Ingrese la contraseña: \n",mask="*")).strip()
            listaKeys = list(formularioMod.keys())
            inputNombre = Validador.validarCampo(Validador,listaKeys[0],formularioMod)
            inputEmail = ValidadorLoguin.validarLogueo(ValidadorLoguin,formularioMod)
            if inputEmail[1] == self.get_email():  
                print(baseDatos.modificacionUsuario('nombre',f"'{inputNombre}'",'email',f"'{inputEmail[1]}'"))
                break
            else:
                print('\nEstás tratando de modificar un usuario que no te pertenece!\nIntente nuevamente!')                         
                    
    def modificarApellido(self):
        formularioMod = {}
        while True:
            formularioMod['apellido'] = (input('Ingrese su apellido nuevo:  ')).strip()
            formularioMod['email'] = (input('Ingrese su correo electronico:  ')).strip()
            formularioMod['password'] = (stdiomask.getpass(prompt="Ingrese la contraseña: \n",mask="*")).strip()
            listaKeys = list(formularioMod.keys())
            inputApellido = Validador.validarCampo(Validador,listaKeys[0],formularioMod)
            inputEmail = ValidadorLoguin.validarLogueo(ValidadorLoguin,formularioMod)
            if inputEmail[1] == self.get_email():  
                print(baseDatos.modificacionUsuario('apellido',f"'{inputApellido}'",'email',f"'{inputEmail[1]}'"))
                break
            else:
                print('\nEstás tratando de modificar un usuario que no te pertenece!\nIntente nuevamente!')                         
                    
    def modificarEmail(self):
        formularioMod = {}
        while True:
            formularioMod['email'] = (input('Ingrese su mail nuevo:  ')).strip()
            formularioMod['celular'] = (input('Ingrese su celular:  ')).strip()
            formularioMod['password'] = (stdiomask.getpass(prompt="Ingrese la contraseña: \n",mask="*")).strip()
            formularioMod2 = {
                'celular': formularioMod['celular'],
                'password': formularioMod['password']}
            inputEmail = Validador.validarEmail(Validador,'email',formularioMod) #chico@gmail.com
            inputCelular = ValidadorLoguin.validarLogueo(ValidadorLoguin,formularioMod2)[-1]
            if inputCelular == self.get_celular():
                print(baseDatos.modificacionUsuario('email',f"'{inputEmail}'",'celular',f"'{inputCelular}'"))
                break
            else:
                print('\nEstás tratando de modificar un usuario que no te pertenece!\nIntente nuevamente!')                         

    def modificarCelular(self):
        formularioMod = {}
        while True:
            formularioMod['celular'] = (input('Ingrese su celular nuevo:  ')).strip()
            formularioMod['email'] = (input('Ingrese su mail:  ')).strip()
            formularioMod['password'] = (stdiomask.getpass(prompt="Ingrese la contraseña: \n",mask="*")).strip()
            formularioMod2 = {
                'email': formularioMod['email'],
                'password': formularioMod['password']}
            inputCelular = Validador.validarCelular(Validador,'celular',formularioMod) 
            inputEmail = ValidadorLoguin.validarLogueo(ValidadorLoguin,formularioMod2)[-1]
            if inputEmail == self.get_email():
                print(baseDatos.modificacionUsuario('celular',f"'{inputCelular}'",'email',f"'{inputEmail}'"))
                break
            else:
                print('\nEstás tratando de modificar un usuario que no te pertenece!\nIntente nuevamente!')                         
    
    def modificarPassword(self):
        while True:
            formulario = {}
            formularioMod = {}
            formulario['password'] = (stdiomask.getpass(prompt='Ingrese su actual password:  ',mask='*')).strip()
            formularioMod['password'] = (stdiomask.getpass(prompt='Ingrese su nueva password:  ',mask='*')).strip()
            formularioMod['cpassword'] = (stdiomask.getpass(prompt='Ingrese nuevamente su password:  ',mask='*')).strip()
            formulario['email'] = 'chiquito@gmail.com' #(input('Ingrese su correo electronico:  ')).strip()
            validacionPassVieja = ValidadorLoguin.validarPassword(ValidadorLoguin,formulario)
            password = base64.b64decode(self.get_password().encode('UTF-8')).decode('UTF-8')
            if formulario['email'] == self.get_email():
                if validacionPassVieja == password:
                    validarPassNueva = Validador.validarPassword(Validador,'password',formularioMod)
                    print(baseDatos.modificarUsuarioPass('contrasenia','ccontrasenia',f"'{validarPassNueva[0]}'",'email',f"'{formulario['email']}'"))
                    break
            else:
                print('Estas tratando de modificar un usuario que no te pertenece!')

    def modificarSexo(self):
        while True:
            formularioMod = {}
            while True:
                opcion= (input('\nSeleecione su nuevo sexo:\nA) Hombre\nB) Mujer\nOpcion:  ').lower()).strip()
                if opcion == 'a':
                    formularioMod['sexo'] = 'H'
                    break
                elif opcion == 'b':
                    formularioMod['sexo'] = 'M'
                    break
                else:
                    print('\nOpcion incorrecta! ')
            formularioMod['email'] = (input('Ingrese su email:  ')).strip()
            formularioMod['password'] =  (stdiomask.getpass(prompt="Ingrese la contraseña: \n",mask="*")).strip()
            listaKeys = list(formularioMod.keys())
            inputSexo = Validador.validarCampo(Validador,listaKeys[0],formularioMod)
            inputEmail = ValidadorLoguin.validarLogueo(ValidadorLoguin,formularioMod)
            if inputEmail[1] == self.get_email():  
                print(baseDatos.modificacionUsuario('sexo',f"'{inputSexo}'",'email',f"'{inputEmail[1]}'"))
                break
            else:
                print('\nEstás tratando de modificar un usuario que no te pertenece!\nIntente nuevamente!')    

    def modificarFotoPerfil(self):
        formularioMod = {}
        while True:
            formularioMod['imagenFotoPerfil'] = (input('Ingrese su nueva foto de perfil:  ')).strip()
            formularioMod['email'] = (input('Ingrese su correo electronico:  ')).strip()
            formularioMod['password'] = (stdiomask.getpass(prompt="Ingrese la contraseña: \n",mask="*")).strip()
            listaKeys = list(formularioMod.keys())
            inputFotoPerfil = Validador.validarCampo(Validador,listaKeys[0],formularioMod)
            inputEmail = ValidadorLoguin.validarLogueo(ValidadorLoguin,formularioMod)
            if inputEmail[1] == self.get_email():  
                print(baseDatos.modificacionUsuario('imagenPerfil',f"'{inputFotoPerfil}'",'email',f"'{inputEmail[1]}'"))
                break
            else:
                print('\nEstás tratando de modificar un usuario que no te pertenece!\nIntente nuevamente!')                         
                         
    def modificarFotoPortada(self):
        formularioMod = {}
        while True:
            formularioMod['imagenFotoPortada'] = (input('Ingrese su nueva foto de portada:  ')).strip()
            formularioMod['email'] = (input('Ingrese su correo electronico:  ')).strip()
            formularioMod['password'] = (stdiomask.getpass(prompt="Ingrese la contraseña: \n",mask="*")).strip()
            listaKeys = list(formularioMod.keys())
            inputFotoPortada = Validador.validarCampo(Validador,listaKeys[0],formularioMod)
            inputEmail = ValidadorLoguin.validarLogueo(ValidadorLoguin,formularioMod)
            if inputEmail[1] == self.get_email():  
                print(baseDatos.modificacionUsuario('imagenPortada',f"'{inputFotoPortada}'",'email',f"'{inputEmail[1]}'"))
                break
            else:
                print('\nEstás tratando de modificar un usuario que no te pertenece!\nIntente nuevamente!') 

    def modificarBiografia(self):
        formularioMod = {}
        while True:
            formularioMod['biografia'] = (input('Ingrese su nueva biografia:  ')).strip()
            formularioMod['email'] = (input('Ingrese su correo electronico:  ')).strip()
            formularioMod['password'] = (stdiomask.getpass(prompt="Ingrese la contraseña: \n",mask="*")).strip()
            listaKeys = list(formularioMod.keys())
            inputbiografia = Validador.validarCampo(Validador,listaKeys[0],formularioMod)
            inputEmail = ValidadorLoguin.validarLogueo(ValidadorLoguin,formularioMod)
            if inputEmail[1] == self.get_email():  
                print(baseDatos.modificacionUsuario('biografia',f"'{inputbiografia}'",'email',f"'{inputEmail[1]}'"))
                break
            else:
                print('\nEstás tratando de modificar un usuario que no te pertenece!\nIntente nuevamente!') 

    def modificarSentimental(self):
        while True:
            formularioMod = {}
            formulario = {}
            print("\nSituacion sentimental:")
            cont = 1
            for x in baseDatos.selectNombreSentimental():
                for y in x:
                    print(f"\t• {cont}: {y}")
                cont += 1
            formulario["sentimental"] = (input("Ingrese el número de su situacion sentimental:  ")).strip()
            listaKeys = list(formulario.keys())
            inputSentimental = int(Validador.validarCampo(Validador,listaKeys[0],formulario))
            formularioMod['email'] = (input('Ingrese su correo electronico:  ')).strip()
            formularioMod['password'] = (stdiomask.getpass(prompt="Ingrese la contraseña: \n",mask="*")).strip()
            inputEmail = ValidadorLoguin.validarLogueo(ValidadorLoguin,formularioMod)[1]
            # print(inputSentimental)
            if inputEmail == self.get_email():
                print(baseDatos.modificacionUsuario('sentimental_ID',inputSentimental,'email',f"'{inputEmail}'"))
                break
            else:
                print('\nEstás tratando de modificar un usuario que no te pertenece!\nIntente nuevamente!') 

    def modificarCiudad(self):
        while True:
            formulario = {}
            formularioMod = {}
            print("\nCiudad:")
            cont = 1
            for x in baseDatos.selectNombreCiudad():
                for y in x:
                    print(f"\t• {cont}: {y}")
                cont += 1
            formulario["ciudad"] = (input("Ingrese el numero de su ciudad:  ")).strip()
            listaKeys = list(formulario.keys())
            inputCiudad = int(Validador.validarCampo(Validador,listaKeys[0],formulario))
            formularioMod['email'] = (input('Ingrese su mail:  ')).strip()
            formularioMod['password'] = (stdiomask.getpass(prompt="Ingrese la contraseña: \n",mask="*")).strip()
            inputEmail = ValidadorLoguin.validarLogueo(ValidadorLoguin,formularioMod)[1]
            if inputEmail == self.get_email():
                print(baseDatos.modificacionUsuario('ciudad_ID',inputCiudad,'email',f"'{inputEmail}'"))
                break
            else:
                print('\nEstás tratando de modificar un usuario que no te pertenece!\nIntente nuevamente!') 
    
    #DAR BAJA DE USUARIO

    def menuBaja(self):
        while True:
            opcion = input('\n¿Estás seguro que deseas eliminar tu cuenta?\n\t1) Si\n\t2) No\nOpcion:  ')
            if opcion == '1':
                self.bajaUsuario()
            elif opcion == '2':
                print('Nos vemos pronto!')
                break
            else:
                print('Opcion incorrecta!')

    def bajaUsuario(self):
        while True:
            formulario = {}
            formulario['email'] = (input('Ingrese su mail:  ')).strip()
            formulario['password'] = (stdiomask.getpass(prompt="Ingrese la contraseña: \n",mask="*")).strip()
            validarEmail = ValidadorLoguin.validarLogueo(ValidadorLoguin,formulario)[1]
            if validarEmail == self.get_email():
                print(baseDatos.borrarUsuario(f"'{validarEmail}'"))
                break
            else:
                print('\nEstás tratando de modificar un usuario que no te pertenece!\nIntente nuevamente!') 

    #AGREGAR AMIGO

    def agregarAmigo(self):
        while True:
            formulario = {}
            formularioMod = {}
            cont = 1
            print('\nAMIGOS PARA AGREGAR:')
            for x in baseDatos.selectNombreUsuario(f"'{self.get_nombre()}'"):
                for y in x:
                    print(f"\t• {cont}: {y}")
                cont += 1
            formulario['amigo'] = (input('Ingrese el numero del amigo que quiere ingresar:  ')).strip()
            listaKeys = list(formulario.keys())
            inputAmigo = int(Validador.validarCampo(Validador,listaKeys[0],formulario))
            nombreAmigo = baseDatos.selectNombreUsuario(f"'{self.get_nombre()}'")[inputAmigo-1][0]
            idUsuarioAmigo = baseDatos.selectIDUsuarioAmigo(f"'{nombreAmigo}'")
            # idUsuario = baseDatos.selectIDUsuarioAct(f"'{self.get_nombre()}'")
            formularioMod['email'] = (input('Inserte su email:  ')).strip()
            formularioMod['password'] = (stdiomask.getpass(prompt="Ingrese la contraseña: \n",mask="*")).strip()
            inputEmail = ValidadorLoguin.validarLogueo(ValidadorLoguin,formularioMod)
            if inputEmail[1] == self.get_email():  
                print(baseDatos.insertAmigos(self.get_id(),idUsuarioAmigo))
                break
            else:
                print('\nEstás tratando de modificar un usuario que no te pertenece!\nIntente nuevamente!') 

    def eliminarAmigo(self):
        while True:
            # idUsuario = baseDatos.selectIDUsuarioAct(f"'{self.get_nombre()}'")
            formulario = {}
            formularioMod = {}
            cont = 1
            if baseDatos.listaAmigos(self.get_id()) == []:
                print('No tiene amigos para eliminar, puedes agregar amigos!')
                break
            else:
                print('\nAMIGOS DISPONIBLES PARA ELIMINAR:')
                for x in baseDatos.listaAmigos(self.get_id()):
                    for y in x:
                        print(f"\t• {cont}: {y}")
                    cont += 1
                formulario['amigo'] = (input('Ingrese el numero del amigo que quiere eliminar:  ')).strip()
                listaKeys = list(formulario.keys())
                inputAmigo = int(Validador.validarCampo(Validador,listaKeys[0],formulario))
                nombreAmigo = baseDatos.listaAmigos(self.get_id())[inputAmigo-1][0]
                idUsuarioAmigo = baseDatos.selectIDUsuarioAmigo(f"'{nombreAmigo}'")
                formularioMod['email'] = (input('Inserte su email:  ')).strip()
                formularioMod['password'] = (stdiomask.getpass(prompt="Ingrese la contraseña: \n",mask="*")).strip()
                inputEmail = ValidadorLoguin.validarLogueo(ValidadorLoguin,formularioMod)
                if inputEmail[1] == self.get_email():  
                    print(baseDatos.eliminarAmigo(self.get_id(),idUsuarioAmigo))
                    break
                else:
                    print('\nEstás tratando de modificar un usuario que no te pertenece!\nIntente nuevamente!')

    def listadoAmigos(self):
        # idUsuario = baseDatos.selectIDUsuarioAct(f"'{self.get_nombre()}'")
        cont = 1
        if baseDatos.listaAmigos(self.get_id()) == [] :
            print('\nNo tienes amigos! Puedes agregarlos!')
        else:
            print('\nAMIGOS:')
            for x in baseDatos.listaAmigos(self.get_id()):
                for y in x:
                    print(f"\t• {cont}: {y}")
                cont += 1

