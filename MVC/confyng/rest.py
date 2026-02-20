from flask import Flask, jsonify
from confyng.confyg import get_db_connection
app = Flask(__name__)
@app.route('/studenti', methods=['GET'])
def get_studenti():
    studenti = lista_studenti()
    return jsonify(studenti), 200

        