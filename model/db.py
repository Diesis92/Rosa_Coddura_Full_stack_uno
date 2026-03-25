import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host='localhost',          # oppure '127.0.0.1'
        port=3306,                 # se hai esposto la porta nel docker-compose
        user='myuser',
        password='mypassword',
        database='scuola'
    )