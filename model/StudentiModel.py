from dataclasses import fields

from db import get_connection

class StudentiModel:

    # INSERT
    def insert(self, nome, cognome, email):
        conn = get_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO studenti (nome, cognome, email) VALUES (%s, %s, %s)"
        cursor.execute(sql, (nome, cognome, email))
        conn.commit()
        conn.close()


    # READ ALL
    def get_all(self):
        conn = get_connection()
        cursor = conn.cursor()
        sql = "SELECT * FROM studenti"
        cursor.execute(sql)
        result = cursor.fetchall()
        conn.close()
        return result

    # READ ONE
    def get_one(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        sql = "SELECT * FROM studenti WHERE id = %s"
        cursor.execute(sql, (id,))
        result = cursor.fetchall()
        conn.close()
        return result
    #Update
    def update(self, id, nome, cognome, email):
        conn = get_connection()
        cursor = conn.cursor()
        sql = "UPDATE studenti SET nome = %s, cognome = %s, email = %s WHERE id = %s"
        cursor.execute(sql, (nome, cognome, email, id))
        conn.commit()
        conn.close()

    #PATCH
    def patch_student(self, id, data):
        conn = get_connection()
        cursor = conn.cursor()
        fields = []
        values = []
        for key, value in data.items():
            fields.append(f"{key} = %s")
            values.append(value)
        values.append(id)
        sql = f"UPDATE studenti SET {', '.join(fields)} WHERE id = %s"
        cursor.execute(sql, values)
        conn.commit()
        conn.close()

    #delete
    def delete(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        sql = "DELETE FROM studenti WHERE id = %s"
        cursor.execute(sql, (id,))
        conn.commit()
        conn.close()
