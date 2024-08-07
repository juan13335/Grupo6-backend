class Tabla:
    def __init__(self,n_tabla, n_campo, n_conexion):
        self.tabla = n_tabla
        self.campo = n_campo
        self.conexion = n_conexion

    def crear(self, valores):
        for campo, valor in zip(self.campos, valores):
            setattr(self, campo, valor)

    def guardar_db(self):
        pass

    @classmethod
    def obtener(cls, campo=None, valor=None):
        if campo == None or valor == None:
            consulta = f"SELECT * FROM {cls.tabla};"
            return cls.__conectar(consulta)
        else:
            consulta = (f"SELECT * FROM {cls.tabla}"
                        f"WHERE {campo} = %s")
            return cls.__conectar(consulta, (valor))

    @classmethod
    def actualizar_db(cls):
        pass

    @classmethod
    def eliminar(cls):
        pass

    @classmethod
    def __conectar(cls, consulta, datos=None):
        try:
            cursor = cls.conexion.cursor()
        except Exception as e:
            cls.conexion.connect()
            cursor = cls.conexion.cursor()

        cursor.execute(consulta)
        datos = cursor.fetchall()
        print(f"Datos recuperados de la base de datos: {datos}")
        resultado = [cls(dato) for dato in datos]
        cls.conexion.close()
        return resultado
