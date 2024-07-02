from flask import jsonify

from main import app
from componentes.modelos import Usuario
#from componentes.modelos import Suscripcion

@app.route('/usuarios', methods=['GET'])
def mostrar_usuarios():
    usuarios = Usuario.obtener() 
    print(f"Datos recuperados de la base de datos: {usuarios}") # Para verificar que devuelve
    usuarios_dicc = [u.__dict__ for u in usuarios]
    print(f"Usuarios en formato diccionario: {usuarios_dicc}")# Devuelve vacio 
    return jsonify(usuarios_dicc)

