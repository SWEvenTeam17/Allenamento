import mysql.connector

def get_user_name(user_id):
    conn = mysql.connector.connect(
        host="localhost",
        user="utente",
        password="password",
        database="database"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM users WHERE id = %s", (user_id,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result[0] if result else None
