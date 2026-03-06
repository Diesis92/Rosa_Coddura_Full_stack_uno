from flask import Flask, request, jsonify

app = Flask(__name__)

users = [
    {"id": 1, "nome": "Mario"},
    {"id": 2, "nome": "Luigi"}
]

#GET

@app.route("/api/studenti")
def studenti():
    dati = {
        "id": 1,
        "nome": "Giovanni",
        "cognome": "Vacanti"
    }  # <-- chiudiamo il dizionario prima del return
    return jsonify(dati)  # <-- return fuori dal dizionario

#POST

@app.route("/api/saluta", methods=["POST"])  # <-- correggi methods e aggiungi / all'inizio
def saluta():
    dati = request.json               # <-- leggere JSON inviato
    nome = dati["nome"]               # <-- estrarre il campo "nome"
    return {"messaggio": "Ciao " + nome}  # <-- restituire JSON

#PUT

@app.route("/api/utenti/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    dati = request.json                   # legge JSON inviato
    nuovo_nome = dati.get("nome")         # prende il nuovo nome
    for user in users:                    # cerca l'utente con quell'id
        if user["id"] == user_id:
            user["nome"] = nuovo_nome    # aggiorna il nome
            return jsonify(user)          # restituisce l'utente aggiornato
    return {"error": "User not found"}, 404  # se id non esiste

if __name__ == "__main__":
    app.run(debug=True)