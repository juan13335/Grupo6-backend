from flask import render_template

from main import app

@app.route('/')
def inicio():
    return render_template('./index.html')