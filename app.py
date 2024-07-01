from flask import Flask
from flask import jsonify
from base_db.dml import obtener_datos

app = Flask(__name__)

# Vistas
@app.route('/')
def inicio():
    return '<h1>Bienvenidos a flask!!</h1>'

@app.route('/datos')
def mostrardatos():
    return jsonify(obtener_datos())

#if __name__ == '__main__':
#    app.run()