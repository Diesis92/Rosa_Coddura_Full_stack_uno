from flask import Flask, request, jsonify

#“Prendi alcune cose dalla libreria Flask perché voglio usarle, con request prendi i dati dal database e traducili in json”.

#"Crea la mia applicazione web con il server flask
app = Flask(__name__)

#dati fittizzi

user = [
    {"id":1,"name":"Mario"},
    {"id":2,"name":"Paolo"}
]

#Quando qualcuno visita questo URL, esegui questa funzione.
#controller /rotta, metodo = ["GET "]
@app.route("/users , method = [ "GET"]")
# funzione per prendere la lista degli utenti
def get_users():
    return jsonify(users)

#per prendere dei determinati nomi = rotta,/<tipo per indice quindi int:user_id/+ metodo 
#app.route("/percorso/<tipo:nome>"), metodo = ["GET "] def funzione(nome):
@app.route("/users/<int:user_id>, metodo = ["GET "] ")
def get_user(user_id):
    return jsonify(user_id)


@app.route("/api/studenti")
def studenti():
    dati = {
    "id":1,
    "nome":"Giovanni",
    "cognome":"vacanti"
    return jsonify(dati)
    }
    
if __name__ == "__main__":
    app.run(debug=True)