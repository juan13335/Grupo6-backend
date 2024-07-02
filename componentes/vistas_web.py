from flask import render_template, request
#import mysql.connector


from main import app

@app.route('/')
def inicio():
    return render_template('./index.html')

#@app.route('/', methods=['GET', 'POST'])
#def crear_registro():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    email = request.form['email']
    password = request.form['password']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO usuario (usuario, apellido, email, password) VALUES (%s, %s, %s, %s)", (nombre, apellido, email, password))
    mysql.connection.commit()
    return render_template("index.html")



