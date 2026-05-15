from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

@app.route("/studenti/")
def studenti():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="supersecret",
            database="scuola"
        )

        cursor = conn.cursor()
        cursor.execute("SELECT nome FROM studenti")
        rows = cursor.fetchall()
        
        data = []
        for r in rows:
            data.append({"nome": r[0]})

        return jsonify(data)
    
    except mysql.connector.Error as err:
        return jsonify({"error": f"Database error: {err}"}), 500
    
    except Exception as err:
        return jsonify({"error": f"Server error: {str(err)}"}), 500
    
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == "__main__":
    app.run(port=5000, debug=True)