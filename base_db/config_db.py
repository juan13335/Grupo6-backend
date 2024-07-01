import mysql.connector

config_dev = {
    "user" : 'root',
    "password" : 'ritarita1010',
    "host" : '127.0.0.1',
    "database" : 'noticias',
}


config_prod = {
    "user" : 'juan13335',
    "password" : 'grupo6backend',
    "host" : 'juan13335.mysql.pythonanywhere-services.com',
    "database" : 'juan13335$noticiero',
}

conexion = mysql.connector.connect(**config_dev)
