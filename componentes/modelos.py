from base_db.dml import Tabla
from base_db.config_db import conexion as con 

class Usuario(Tabla):
    tabla = 'usuario'
    campos = ('id_usuario', 'nombre', 'apellido', 'contrasenia', 'categoria', 'fecha_registro')
    conexion = con

    def __init__(self, valores):
        super().crear(valores)

class Suscripcion(Tabla):
    tabla = 'suscripcion'
    campos = ('id_suscripcion', 'email', 'fecha_inicio', 'fecha_final', 'estado')
    conexion = con

    def __init__(self, valores):
        super().crear(valores)

