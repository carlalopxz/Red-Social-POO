import mysql.connector

configuracion = {
    "host":"localhost",
    "user": "root",
    "password": "",
    "database": "redsocial"
}

class DB():
    def __init__(self):
        self.__conexion = mysql.connector.connect(**configuracion)
        self.__cursor = self.__conexion.cursor()

    
    def get_conexion(self):
        return self.__conexion
    def get_cursor(self):
        return self.__cursor

    def selectNombreCiudad(self):
        sql = 'SELECT nombre FROM ciudad'
        baseDatos.get_cursor().execute(sql)
        resultado = baseDatos.get_cursor().fetchall()
        return resultado

    def selectIDCiudad(self,nombreCiudad):
        sql = 'SELECT id FROM ciudad WHERE nombre = %s'
        val = (nombreCiudad,)
        baseDatos.get_cursor().execute(sql,val)
        resultado = baseDatos.get_cursor().fetchall()
        return resultado

    def selectNombreSentimental(self):
        sql = 'SELECT nombre FROM sentimental'
        baseDatos.get_cursor().execute(sql)
        resultado = baseDatos.get_cursor().fetchall()
        return resultado
    
    def insertUsuario(self,formulario):
        sql = '''INSERT INTO usuario(nombre,apellido,email,celular,contrasenia,ccontrasenia,
        sexo,imagenPerfil,imagenPortada,biografia,fechaCreacionCuenta,sentimental_ID,ciudad_ID) 
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
        baseDatos.get_cursor().execute(sql,formulario)
        baseDatos.get_conexion().commit()
        resultado = baseDatos.get_cursor().rowcount, "Registro Exitoso!"
        return resultado

    def selectNombreConEmail(self,correo):
        sql = 'SELECT nombre,contrasenia FROM usuario where email = %s'
        val = (correo,)
        baseDatos.get_cursor().execute(sql,val)
        resultado = baseDatos.get_cursor().fetchall()
        return resultado

    def selectNombreConCelular(self,celular):
        sql = 'SELECT nombre,contrasenia FROM usuario where celular = %s'
        val = (celular,)
        baseDatos.get_cursor().execute(sql,val)
        resultado = baseDatos.get_cursor().fetchall()
        return resultado
    
    def selectEmail(self,key,formulario):
        sql = "SELECT email FROM usuario WHERE email = %s"
        val = (formulario[key],)
        baseDatos.get_cursor().execute(sql,val)
        return baseDatos.get_cursor().fetchall()

    def selectCelular(self,key,formulario):
        sql = "SELECT celular FROM usuario WHERE celular = %s"
        val = (formulario[key],)
        baseDatos.get_cursor().execute(sql,val)
        return baseDatos.get_cursor().fetchall()
    
    def selectTodoUsuario(self):
        sql = '''SELECT nombre,apellido,email,celular,contrasenia,ccontrasenia,
        sexo,imagenPerfil,imagenPortada,biografia,fechaCreacionCuenta,sentimental_ID,ciudad_ID FROM usuario'''
        baseDatos.get_cursor().execute(sql)
        return baseDatos.get_cursor().fetchall()
    
    def selectIDUsuarioMax(self):
        sql = '''SELECT MAX(id) FROM usuario'''
        baseDatos.get_cursor().execute(sql)
        return baseDatos.get_cursor().fetchall()[0][0] 

    def modificacionUsuario(self,campoAMod,datoNuevo,campoEmailCel,correoCelUsuario):
        sql = 'UPDATE usuario SET {} = {} WHERE {} = {}'.format(campoAMod,datoNuevo,campoEmailCel,correoCelUsuario)
        baseDatos.get_cursor().execute(sql)
        baseDatos.get_conexion().commit()
        resultado = baseDatos.get_cursor().rowcount, 'Registro afectado!'
        return resultado

    def modificarUsuarioPass(self,campoAMod1,campoAMod2,datoNuevo,campoEmailCel,correoCelUsuario):
        sql= 'UPDATE usuario SET {} = {}, {} = {} WHERE {} = {}'.format(campoAMod1,datoNuevo,campoAMod2,datoNuevo,campoEmailCel,correoCelUsuario)
        baseDatos.get_cursor().execute(sql)
        baseDatos.get_conexion().commit()
        resultado = baseDatos.get_cursor().rowcount, 'Registro afectado!'
        return resultado

    def borrarUsuario(self,email):
        sql = "DELETE FROM usuario WHERE email = {}".format(email)
        baseDatos.get_cursor().execute(sql)
        baseDatos.get_conexion().commit()
        if baseDatos.get_cursor().rowcount == 1:
            resultado = "Cuenta Eliminada"
            return resultado
        else:
            resultado = 'Ocurrio un problema al eliminar la cuenta!'
            return resultado
    
    def selectNombreUsuario(self,usuarioAct):
        sql = 'SELECT CONCAT(nombre,SPACE(1),apellido) FROM usuario WHERE nombre <> {}'.format(usuarioAct)
        baseDatos.get_cursor().execute(sql)
        return baseDatos.get_cursor().fetchall()

    def selectIDUsuarioAct(self,usuarioAct):
        sql = 'SELECT id FROM usuario WHERE nombre = {}'.format(usuarioAct)
        baseDatos.get_cursor().execute(sql)
        return baseDatos.get_cursor().fetchall()[0][0]

    def selectIDUsuarioAmigo(self,usuarioAmigo):
        sql = 'SELECT id FROM usuario WHERE CONCAT(nombre,SPACE(1),apellido) = {}'.format(usuarioAmigo)
        baseDatos.get_cursor().execute(sql)
        return baseDatos.get_cursor().fetchall()[0][0]
    
    def insertAmigos(self,usuarioID, amigoID):
        sql = 'INSERT INTO amigos (usuario_ID,amigos_ID) VALUES ({},{})'.format(usuarioID,amigoID)
        baseDatos.get_cursor().execute(sql)
        baseDatos.get_conexion().commit()
        if baseDatos.get_cursor().rowcount == 1:
            resultado = 'Amigo agregado con exito!'
            return resultado

    def listaAmigos(self,usuarioAct):
        sql= '''SELECT concat(usuario.nombre, SPACE(1),usuario.apellido) 
        FROM usuario JOIN amigos ON amigos.amigos_id = usuario.id
        WHERE amigos.usuario_id = {}'''.format(usuarioAct)
        baseDatos.get_cursor().execute(sql)
        return baseDatos.get_cursor().fetchall()

    def eliminarAmigo(self,usuarioID,amigoID):
        sql = '''DELETE FROM amigos 
        WHERE usuario_id = {} AND amigos_id = {}'''.format(usuarioID,amigoID)
        baseDatos.get_cursor().execute(sql)
        baseDatos.get_conexion().commit()
        if baseDatos.get_cursor().rowcount == 1:
            resultado = 'Amigo eliminado!'
            return resultado
        else:
            print('Hubo un problema al eliminar al amigo')
baseDatos = DB()
