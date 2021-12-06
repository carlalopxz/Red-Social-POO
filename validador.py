from validate_email import validate_email
import re,base64,stdiomask
from baseDeDatos import baseDatos

class Validador():
    def __init__(self):
        pass

    def validarFormulario(self,formulario):
        for key in formulario.keys():
            if key == "email":
                 self.validarEmail(self,key,formulario)
            elif key == "password":
                self.validarPassword(self,key,formulario)
            elif key == 'celular':
                self.validarCelular(self,key,formulario)
            elif key == 'imagenPerfil' or key == 'imagenPortada' or key == 'biografia':
                self.validarCamposNull(self,key,formulario)
            else:
                 self.validarCampo(self,key,formulario)
        resultado = baseDatos.insertUsuario(tuple(formulario.values()))
        print(resultado)


    def validarCampo(self,campo,formulario):
        if formulario[campo] == None or formulario[campo] == "":
            print(f"\n¡Error! falto completar el '{campo}'")
            formulario[campo] = input(f"Complete el {campo}:  ")
            self.validarCampo(self,campo,formulario)
        return formulario[campo]
    
    def validarEmail(self,campo,formulario):
        if formulario[campo] == None or formulario[campo] == "":
            print(f"\n¡Error! falto completar el '{campo}'")
            formulario[campo] = input(f"Complete el {campo}:  ")
            self.validarEmail(self,campo,formulario)
        elif validate_email(formulario[campo], verify=True) == False:
            print("\n¡Error! su e-mail no tiene formato de e-mail")
            formulario[campo] = input(f"Complete el {campo} (usuario@correo.com):  ")
            self.validarEmail(self,campo,formulario)
        return formulario[campo]
    
    def validarPassword(self,campo,formulario):
        if formulario[campo] == None or formulario[campo] == "":
            print(f"\n¡Error! falto completar el '{campo}'")
            formulario[campo] = (stdiomask.getpass(prompt="Ingrese su password que contenga al menos una minuscula, una mayuscula y alguno de los siguientes caracteres especiales '$ % # @': \n", mask = "*")).strip()
            formulario["cpassword"] = (stdiomask.getpass(prompt="Ingrese nuevamente la contraseña: \n",mask="*"))
            self.validarPassword(self,campo,formulario)
        elif len(formulario[campo]) < 6:
            print("\n¡Error! La contraseña debe tener mas de 6 caracteres.")
            formulario[campo] = (stdiomask.getpass(prompt="Ingrese su password que contenga al menos una minuscula, una mayuscula y alguno de los siguientes caracteres especiales '$ % # @': \n", mask = "*")).strip()
            formulario["cpassword"] = (stdiomask.getpass(prompt="Ingrese nuevamente la contraseña: \n",mask="*"))
            self.validarPassword(self,campo,formulario)
        elif formulario[campo] != formulario["cpassword"]:
            print("\n¡Error! Las contraseñas no coinciden.")
            formulario[campo] = (stdiomask.getpass(prompt="Ingrese su password que contenga al menos una minuscula, una mayuscula y alguno de los siguientes caracteres especiales '$ % # @': \n", mask = "*")).strip()
            formulario["cpassword"] = (stdiomask.getpass(prompt="Ingrese nuevamente la contraseña: \n",mask="*"))
            self.validarPassword(self,campo,formulario)
        else:
            if re.search('[a-z]',formulario["password"]) == None or re.search('[A-Z]',formulario["password"]) == None or re.search('[0-9]',formulario["password"]) == None or re.search('[$%#@]',formulario["password"])==None:
                print("\n¡Error! La contraseña debe tener al menos una minuscula, una mayuscula y algunos de los caracteres especiales '$ % # @'")
                formulario[campo] = (stdiomask.getpass(prompt="Ingrese de nuevo su password: \n", mask = "*")).strip()
                formulario["cpassword"] = (stdiomask.getpass(prompt="Ingrese nuevamente la contraseña: \n",mask="*")).strip()
                self.validarPassword(self,campo,formulario)
            else:
                formulario[campo] = base64.b64encode(formulario[campo].encode("UTF-8")).decode("UTF-8")
                formulario["cpassword"] = base64.b64encode(formulario["cpassword"].encode('UTF-8')).decode('UTF-8')
        return formulario['password'],formulario['cpassword']
    def validarCelular(self,campo,formulario):
        if formulario[campo] == None or formulario[campo] == "":
            print(f"\n¡Error! falto completar el '{campo}'")
            formulario[campo] = input(f"Complete el {campo}:  ")
            self.validarCelular(self,campo,formulario)
        elif formulario[campo].isdigit() == False:
            print('\n¡Error! El número contiene al menos una letra.')
            formulario[campo] = input('Ingrese su numero de celular: ')
            self.validarCelular(self,campo,formulario)
        elif len(formulario[campo]) < 11:
            print('\n¡Error! El número debe contener al menos 11 digitos.')
            formulario[campo] = input('Ingrese su numero de celular: ')
            self.validarCelular(self,campo,formulario)
        return formulario[campo]
    
    def validarCamposNull(self,campo,formulario):
        if formulario[campo] == '':
            formulario[campo] = None
