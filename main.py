from flask import Flask

app = Flask(__name__)

#importar vistas
from componentes.vistas_api import *
from componentes.vistas_web import *

#if __name__ == '__main__':
#    app.run()