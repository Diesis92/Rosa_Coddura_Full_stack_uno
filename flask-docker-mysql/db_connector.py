import time
import mysql.connector

# Database connection configuration
db_config = {
    'host': 'db',
    'user': 'root',
    'password': 'password',
    'database': 'visite_db'
}

#restituisce la connessione al database
def get_db_connection():
    for i in range(5):
        try:
            connection = mysql.connector.connect(**db_config)
            return connection
        except mysql.connector.Error:
            print("Database non pronto, riprovo...")
            time.sleep(3)
    return None