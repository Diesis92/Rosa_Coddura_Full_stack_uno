from db.connection import db
import re

def get_all_users():
    print("\n--- TUTTI GLI UTENTI ---")
    for u in db.utenti.find():
        print(u)


def get_by_city(city):
    print(f"\n--- UTENTI DI {city} ---")
    for u in db.utenti.find({"citta": city}):
        print(u)


def get_by_age(min_age):
    print(f"\n--- ETA >= {min_age} ---")
    for u in db.utenti.find({"eta": {"$gte": min_age}}):
        print(u)


def get_name_starting_with(letter):
    print(f"\n--- NOMI CHE INIZIANO PER {letter} ---")
    for u in db.utenti.find({"nome": re.compile(f"^{letter}", re.I)}):
        print(u)