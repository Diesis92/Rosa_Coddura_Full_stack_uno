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
    try:
        connection = mysql.connector.connect(**db_config)
        return connection
    except mysql.connector.Error as err:
        print(f"Errore di connessione al database: {err}")
        return None
    finally:
        print("Tentativo di connessione al database completato.")