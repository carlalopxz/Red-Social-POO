from logging import Formatter
import stdiomask
from baseDeDatos import baseDatos
import base64

class ValidadorLoguin():
    def __init__(self):
        pass

    def validarLogueo(self,formulario):
        for key in formulario.keys():
            if key == "email":
                email=  self.validarEmail(self,key,formulario)
                self.validarPassword(self,formulario)
                return True, email
            elif key == "celular":
                celular = self.validarCelular(self,key,formulario)
                self.validarPassword(self,formulario)  
                return True,celular        
    
    def validarEmail(self,key,formulario):
        if formulario[key] == '' or formulario[key] == None:
            print('\nDebe llenar el campo EMAIL!')
            formulario[key] = (input("Intente de nuevo con su correo:  ")).strip()
            formulario['password'] = (stdiomask.getpass(prompt="Ingrese nuevamente la contraseña: \n",mask="*")).strip()
            self.validarPassword(self,formulario)
            self.validarEmail(self,key,formulario)
        else:
            if baseDatos.selectEmail(key,formulario) == []:
                print('\nEste correo no existe en nuestra base de datos.')
                formulario[key] = (input("Intente de nuevo con su correo:  ")).strip()
                formulario['password'] =(stdiomask.getpass(prompt="Ingrese nuevamente la contraseña: \n",mask="*")).strip()
                self.validarPassword(self,formulario)
                self.validarEmail(self,key,formulario)
        return formulario[key]

    def validarPassword(self,formulario):
        password = None
        keys = list(formulario.keys())
        if keys[0] == 'email' or keys[1] == 'email':
            if formulario['password'] == '':
                print('\nContraseña incorrecta, intente nuevamente')
                formulario['password'] = (stdiomask.getpass(prompt="Ingrese nuevamente la contraseña: \n",mask="*")).strip()
            else:
                password = base64.b64decode(baseDatos.selectNombreConEmail(formulario['email'])[0][-1].encode('UTF-8')).decode('UTF-8')
        elif keys[0] == 'celular':
            if formulario['password'] == '':
                print('\nContraseña incorrecta, intente nuevamente')
                formulario['password'] = (stdiomask.getpass(prompt="Ingrese nuevamente la contraseña: \n",mask="*")).strip()
            else:
                password = base64.b64decode(baseDatos.selectNombreConCelular(formulario['celular'])[0][-1].encode('UTF-8')).decode('UTF-8')
        if password != formulario['password'] or formulario['password'] == '' or formulario['password'] == None:
            print('\nContraseña incorrecta, intente nuevamente')
            formulario['password'] = (stdiomask.getpass(prompt="Ingrese nuevamente la contraseña: \n",mask="*")).strip()
            self.validarPassword(self,formulario)
        return formulario['password']
        
    
    def validarCelular(self,key,formulario):
        if formulario[key] == '' or formulario[key] == None:
            print('\nDebe llenar el campo CELULAR!')
            formulario[key] = (input("Ingrese su celular nuevamente:  ")).strip()
            formulario['password'] = (stdiomask.getpass(prompt="Ingrese nuevamente la contraseña: \n",mask="*")).strip()
            self.validarPassword(self,formulario)
            self.validarCelular(self,key,formulario)
        if baseDatos.selectCelular(key,formulario) == []:
            print('\nEste celular no se encuentra en nuestra base de datos')
            formulario[key] = (input('Ingrese nuevamente su celular: ')).strip()
            formulario['password'] = (stdiomask.getpass(prompt="Ingrese nuevamente la contraseña: \n",mask="*")).strip()
            self.validarPassword(self,formulario)
            self.validarCelular(self,key,formulario)
        return formulario[key]
            

