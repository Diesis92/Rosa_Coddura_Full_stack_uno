from flask import Flask, request, jsonify
from StudentiModel import StudentiModel  # se è in model/, fai: from model.StudentiModel import StudentiModel

app = Flask(__name__)
model = StudentiModel()

# --- INSERT ---
@app.route('/studenti', methods=['POST'])
def insert():
    data = request.get_json()
    stud_id = model.insert(data['nome'], data['cognome'], data['email'])
    return jsonify({'id': stud_id})

# --- GET ALL ---
@app.route('/studenti', methods=['GET'])
def get_all():
    studenti = model.get_all()
    return jsonify(studenti)

# --- GET ONE ---
@app.route('/studenti/<int:id>', methods=['GET'])
def get_one(id):
    studente = model.get_one(id)
    return jsonify(studente)

# --- UPDATE ---
@app.route('/studenti/<int:id>', methods=['PUT'])
def update(id):
    data = request.get_json()
    model.update(id, data['nome'], data['cognome'], data['email'])
    return jsonify({'id': id})

# --- PATCH ---
@app.route('/studenti/<int:id>', methods=['PATCH'])
def patch_student(id):
    data = request.get_json()
    model.patch_student(id, data)
    return jsonify({'id': id})

# --- DELETE ---
@app.route('/studenti/<int:id>', methods=['DELETE'])
def delete(id):
    model.delete(id)
    return jsonify({'id': id})

if __name__ == "__main__":
    app.run(debug=True)