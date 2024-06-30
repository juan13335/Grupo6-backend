import mysql.connector 

config_db = {
    "user" : 'root',
    "password" : 'Ritarita1010',
    "host" : '127.0.0.1',
    "database" : 'noticias',
}

conexion = mysql.connector.connect(**config_db)
