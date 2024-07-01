class Tabla:
    def __init__(self,n_tabla, n_campo, n_conexion):
        self.tabla = n_tabla
        self.campo = n_campo
        self.conexion = n_conexion

    @classmethod
    def crear(cls):
        pass

    @classmethod
    def guardar_db(cls):
        pass

    @classmethod
    def obtener(cls):
        consulta = f"SELECT * FROM {cls.tabla};"
        return cls.__conectar(consulta)

    @classmethod
    def actualizar_db(cls):
        pass

    @classmethod
    def eliminar(cls):
        pass

    @classmethod
    def __conectar(cls, consulta):
        try:
            cursor = cls.conexion.cursor()
        except Exception as e:
            cls.conexion.connect()
            cursor = cls.conexion.cursor()

        cursor.execute(consulta)
