from pymongo import ASCENDING, DESCENDING
from app.database.connessione import libri
from app.models.libro import Libro


def inserisci_libri():

    lista_libri = [
        Libro(
            "Il Signore degli Anelli",
            "Tolkien",
            1954,
            "Fantasy",
            3,
            2
        ).to_dict(),

        Libro(
            "1984",
            "Orwell",
            1949,
            "Distopia",
            5,
            5
        ).to_dict(),

        Libro(
            "Harry Potter",
            "Rowling",
            1997,
            "Fantasy",
            4,
            1
        ).to_dict()
    ]

    libri.insert_many(lista_libri)


def trova_fantasy_disponibili():

    return list(
        libri.find({
            "genere": "Fantasy",
            "disponibili": {"$gt": 0}
        })
    )


def registra_prestito(titolo):

    libri.update_one(
        {"titolo": titolo},
        {"$inc": {"disponibili": -1}}
    )


def aggrega_per_genere():

    pipeline = [
        {
            "$group": {
                "_id": "$genere",
                "totCopie": {"$sum": "$copie"},
                "totDisponib": {"$sum": "$disponibili"},
                "numLibri": {"$sum": 1}
            }
        },
        {
            "$sort": {"totCopie": -1}
        }
    ]

    return libri.aggregate(pipeline)


def crea_indici():

    libri.create_index([("autore", ASCENDING)])

    libri.create_index([
        ("genere", ASCENDING),
        ("disponibili", DESCENDING)
    ])


def soft_delete(titolo):

    libri.update_one(
        {"titolo": titolo},
        {"$set": {"eliminato": True}}
    )