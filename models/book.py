from config.database import get_connection

def get_books_by_subject(subject):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM Books WHERE subject = %s"
    cursor.execute(query, (subject,))
    books = cursor.fetchall()
    cursor.close()
    conn.close()
    return books


def get_all_books():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM Books"
    cursor.execute(query)
    books = cursor.fetchall()
    cursor.close()
    conn.close()
    return books