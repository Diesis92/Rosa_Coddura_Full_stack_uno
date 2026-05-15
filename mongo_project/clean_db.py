from db.connection import db

db.utenti.delete_many({})
db.prodotti.delete_many({})

print("Database pulito")