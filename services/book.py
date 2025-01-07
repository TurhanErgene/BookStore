from config.database import get_connection

def get_books_by_subject(subject):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM Books WHERE subject = %s"
    cursor.execute(query, (subject,)) # Note the comma after subject to create a tuple with one element 
                                    # Without the trailing comma, (subject,) would just be subject (not a tuple) and cause an error.
    books = cursor.fetchall()
    cursor.close()
    conn.close()
    return books


def get_all_subjects():
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT DISTINCT subject FROM Books ORDER BY subject"
    cursor.execute(query)
    subjects = cursor.fetchall()
    cursor.close()
    conn.close()
    return [subject[0] for subject in subjects]  # Returns a list of subjects


def get_all_books():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM Books"
    cursor.execute(query)
    books = cursor.fetchall()
    cursor.close()
    conn.close()
    return books


