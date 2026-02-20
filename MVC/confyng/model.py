def lista_studenti():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT nome, cognome FROM studenti")
    records = cursor.fetchall()
    studenti = []
    for (nome, cognome) in records:
        studenti.append({"nome": nome, "cognome": cognome})
    cursor.close()
    conn.close()
    return studenti