from config.database import get_connection

def register_member(data):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        INSERT INTO Members (fname, lname, address, city, zip, phone, email, password)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, data)
    conn.commit()
    cursor.close()
    conn.close()

def login_member(email, password):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM Members WHERE email = %s AND password = %s"
    cursor.execute(query, (email, password))
    member = cursor.fetchone()
    cursor.close()
    conn.close()
    return member