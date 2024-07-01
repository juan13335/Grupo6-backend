import mysql.connector

config_db = {
    "user" : 'juan13335',
    "password" : 'grupo6backend',
    "host" : 'juan13335.mysql.pythonanywhere-services.com',
    "database" : 'juan13335$noticiero',
}

conexion = mysql.connector.connect(**config_db)
