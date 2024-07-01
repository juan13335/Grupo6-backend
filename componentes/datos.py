from componentes.config_db import conexion

def obtener_datos():
   con = conexion
   cursor = con.cursor(dictionary=True)
   consulta = "SELECT * FROM usuario"
   cursor.execute(consulta)
   datos = cursor.fetchall()
   con.close()
   try:
      cursor = con.cursor(dictionary=True)
   except Exception:
      con.connect()
      cursor = con.cursor(dictionary=True)  
   return datos
