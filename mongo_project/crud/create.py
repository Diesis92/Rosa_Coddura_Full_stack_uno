from db.connection import db


def insert_users():

    utenti = [
        {
            "nome": "Giovanni Vacanti",
            "email": "g@ecubing.it",
            "eta": 40,
            "ruoli": ["admin", "insegnante"],
            "citta": "Palermo"
        },
        {
            "nome": "Marco",
            "email": "m@mail.it",
            "eta": 25,
            "citta": "Roma"
        },
        {
            "nome": "Laura",
            "email": "l@mail.it",
            "eta": 30,
            "citta": "Milano"
        },
        {
            "nome": "Luca",
            "email": "v@mail.it",
            "eta": 22,
            "citta": "Napoli"
        }
    ]

    for u in utenti:
        # controllo duplicato tramite email
        if db.utenti.find_one({"email": u["email"]}):
            print(f"Utente già esistente: {u['email']}")
        else:
            result = db.utenti.insert_one(u)
            print(f"Inserito utente: {u['email']} -> ID: {result.inserted_id}")


def insert_product():

    prodotto = {
        "_id": "SKU-001",
        "nome": "Corso MongoDB",
        "prezzo": 299.00
    }

    # controllo duplicato su _id
    if db["prodotti"].find_one({"_id": prodotto["_id"]}):
        print(f"Prodotto già esistente: {prodotto['_id']}")
    else:
        db["prodotti"].insert_one(prodotto)
        print(f"Prodotto inserito: {prodotto['_id']}")