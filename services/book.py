from config.database import get_connection


def get_all_subjects():
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT DISTINCT subject FROM Books ORDER BY subject"  # DISTINCT: to eliminate duplicate values
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


def get_books_by_subject(subject):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM Books WHERE subject = %s"
    cursor.execute(
        query, (subject,)
    )  # Note the comma after subject to create a tuple with one element
    # Without the trailing comma, (subject,) would just be subject (not a tuple) and cause an error.
    books = cursor.fetchall()
    cursor.close()
    conn.close()
    return books


def search_by_author(author):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM Books WHERE author = %s OR author LIKE %s"
    cursor.execute(query, (f"%{author}%", f"%{author}%"))
    books = cursor.fetchall()
    cursor.close()
    conn.close()
    return books


def search_by_title(title):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM Books WHERE title = %s OR title LIKE %s"
    cursor.execute(query, (f"%{title}%", f"%{title}%"))
    books = cursor.fetchall()
    cursor.close()
    conn.close()
    return books


def get_books_by_subject_paginated(subject, offset, limit):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM Books WHERE subject = %s LIMIT %s OFFSET %s"
    cursor.execute(query, (subject, limit, offset))
    books = cursor.fetchall()
    cursor.close()
    conn.close()
    return books
