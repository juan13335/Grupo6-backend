from flask import jsonify

from main import app
from componentes.modelos import Usuario
from componentes.modelos import Suscripcion

@app.route('/usuarios')
def mostrar_usuarios():
    usuarios = Usuario.obtener()
    usuarios_dicc = [u.__dict__ for u in usuarios]
    return jsonify(usuarios_dicc)