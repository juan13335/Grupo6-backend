from flask import Flask
from flask import jsonify
from componentes.datos import obtener_datos

app = Flask(__name__) 

# Vistas
@app.route('/')
def inicio():
    return '<h1>Hola mundo'

@app.route('/datos')
def mostrardatos():
    return jsonify(obtener_datos())

if __name__ == '__main__':
    app.run()