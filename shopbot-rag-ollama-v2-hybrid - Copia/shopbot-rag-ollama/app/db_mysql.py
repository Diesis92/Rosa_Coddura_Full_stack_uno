"""
db_mysql.py — Lettura prodotti da MySQL
Usa mysql-connector-python, senza dipendenze extra.
"""

import mysql.connector
from app import config


def get_connection():
    """Crea e restituisce una connessione MySQL."""
    return mysql.connector.connect(
        host=config.MYSQL_HOST,
        port=config.MYSQL_PORT,
        database=config.MYSQL_DATABASE,
        user=config.MYSQL_USER,
        password=config.MYSQL_PASSWORD,
        charset="utf8mb4",
    )


def get_prodotti_disponibili() -> list[dict]:
    """
    Legge i prodotti con disponibile=1 da MySQL.
    Restituisce lista di dict.
    """
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("""
            SELECT id, nome, descrizione, categoria, prezzo, tag
            FROM prodotti
            WHERE disponibile = 1
            ORDER BY id
        """)
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()


def get_tutti_i_prodotti() -> list[dict]:
    """Legge tutti i prodotti (anche non disponibili) — per le statistiche."""
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("""
            SELECT id, nome, categoria, prezzo, disponibile
            FROM prodotti
            ORDER BY id
        """)
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()
