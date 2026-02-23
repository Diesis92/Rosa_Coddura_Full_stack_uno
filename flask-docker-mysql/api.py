# dipendente flask , request e jsonify per creare un'API RESTful
from flask import Flask, request, jsonify, render_template
#importa la funzione get_db_connection dal file db_connector.py per gestire la connessione al database
from db_connector import get_db_connection

#crea un'istanza dell'app Flask
app = Flask (__name__)


#quando qualcuno accede alla root dell'applicazione, viene eseguita la funzione home
@app.route('/') 
def home():
    return render_template('index.html') #restituisce il file index.html come risposta alla richiesta

#metodo POST per aggiungere una visita al database
@app.route('/add_visit',methods=['POST'])
def add_visit():
    data = request.get_json() #ottiene i dati JSON dalla richiesta
    nome = data.get('nome') #estrae il nome dal JSON
    cognome = data.get('cognome') #estrae il cognome dal JSON

    if not nome or not cognome: #controlla se nome o cognome sono mancanti
        return jsonify({'error': 'Nome e cognome sono obbligatori'}), 400 #restituisce un errore se mancano
    
    connection = get_db_connection() #ottiene una connessione al database
    if connection is None: #controlla se la connessione è fallita
        return jsonify({'error': 'Impossibile connettersi al database'}), 500 #restituisce un errore se la connessione fallisce 
    try:
        cursor = connection.cursor() #crea un cursore per eseguire le query
        cursor.execute("INSERT INTO visite (nome, cognome) VALUES (%s, %s)", (nome, cognome)) #esegue una query per inserire i dati nel database
        connection.commit() #conferma la transazione
        return jsonify({'message': 'Visita aggiunta con successo'}), 201 #restituisce un messaggio di successo
    except Exception as e: #gestisce eventuali eccezioni durante l'inserimento dei dati
        print(f"Errore durante l'inserimento dei dati: {e}")
        return jsonify({'error': 'Errore durante l\'inserimento dei dati'}), 500 #restituisce un errore se c'è un problema con l'inserimento
    finally:
        cursor.close() #chiude il cursore
        connection.close() #chiude la connessione al database



#GET
@app.route('/get_visits', methods=['GET'])
def get_visits():
    connection = get_db_connection()
    if connection is None:
        return jsonify({'error': 'Impossibile connettersi al database'}), 500
    #cursor è il puntatore che ci permette di eseguire le query sul database senza dover aprire e chiudere la connessione ogni volta
    try: 
        cursor = connection.cursor(dictionary=True) #crea un cursore che restituisce i risultati come dizionario
        cursor.execute("SELECT * FROM visite") #esegue una query per selezionare tutte le visite dal database
        results = cursor.fetchall() #ottiene tutti i risultati della query
        return jsonify(results), 200 #restituisce i risultati in formato JSON
    except Exception as e:
        print(f"Errore durante il recupero dei dati: {e}")
        return jsonify({'error': 'Errore durante il recupero dei dati'}), 500
    finally:
        cursor.close()
        connection.close()

#PUT
@app.route('/update_visit/<int:id>', methods=['PUT'])
def update_visit(id):
    data = request.get_json()
    nome = data.get('nome')
    cognome = data.get('cognome')

    if not nome or not cognome:
        return jsonify({'error': 'Nome e cognome sono obbligatori'}), 400
    
    connection = get_db_connection()
    if connection is None:
        return jsonify({'error': 'Impossibile connettersi al database'}), 500
    try:
        cursor = connection.cursor()
        cursor.execute("UPDATE visite SET nome = %s, cognome = %s WHERE id = %s", (nome, cognome, id))
        connection.commit()
        if cursor.rowcount == 0:
            return jsonify({'error': 'Visita non trovata'}), 404
        return jsonify({'message': 'Visita aggiornata con successo'}), 200
    except Exception as e:
        print(f"Errore durante l'aggiornamento dei dati: {e}")
        return jsonify({'error': 'Errore durante l\'aggiornamento dei dati'}), 500
    finally:
        cursor.close()
        connection.close()

#PATCH
@app.route('/patch_visit/<int:id>', methods=['PATCH'])
def patch_visit(id):
    data = request.get_json()
    nome = data.get('nome')
    cognome = data.get('cognome')

    if not nome and not cognome:
        return jsonify({'error': 'Almeno uno tra nome e cognome è obbligatorio'}), 400
    
    connection = get_db_connection()
    if connection is None:
        return jsonify({'error': 'Impossibile connettersi al database'}), 500
    try:
        cursor = connection.cursor()
        if nome and cognome:
            cursor.execute("UPDATE visite SET nome = %s, cognome = %s WHERE id = %s", (nome, cognome, id))
        elif nome:
            cursor.execute("UPDATE visite SET nome = %s WHERE id = %s", (nome, id))
        elif cognome:
            cursor.execute("UPDATE visite SET cognome = %s WHERE id = %s", (cognome, id))
        connection.commit()
        if cursor.rowcount == 0:
            return jsonify({'error': 'Visita non trovata'}), 404
        return jsonify({'message': 'Visita aggiornata con successo'}), 200
    except Exception as e:
        print(f"Errore durante l'aggiornamento dei dati: {e}")
        return jsonify({'error': 'Errore durante l\'aggiornamento dei dati'}), 500
    finally:
        cursor.close()
        connection.close()

#DELETE
@app.route('/delete_visit/<int:id>', methods=['DELETE'])
def delete_visit(id):
    connection = get_db_connection()
    if connection is None:
        return jsonify({'error': 'Impossibile connettersi al database'}), 500
    try:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM visite WHERE id = %s", (id,))
        connection.commit()
        if cursor.rowcount == 0:
            return jsonify({'error': 'Visita non trovata'}), 404
        return jsonify({'message': 'Visita eliminata con successo'}), 200
    except Exception as e:
        print(f"Errore durante l'eliminazione dei dati: {e}")
        return jsonify({'error': 'Errore durante l\'eliminazione dei dati'}), 500
    finally:
        cursor.close()
        connection.close()




