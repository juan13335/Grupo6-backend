class Tabla:
    def __init__(self,n_tabla, n_campo, n_conexion):
        self.tabla = n_tabla
        self.campo = n_campo
        self.conexion = n_conexion

    @classmethod
    def crear(self, valores):
        for campo, valor in zip(self.campos, valores):
            setattr(self, campo, valor)

    @classmethod
    def guardar_db(self):
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
        datos = cursor.fetchall()
        # lista por comprehension
        resultado = [cls(dato) for dato in datos]
        return resultado
