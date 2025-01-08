from config.database import get_connection


def add_to_cart(member_id, isbn, quantity):
    conn = get_connection()
    cursor = conn.cursor()

    # Check if the book is already in the cart
    query = "SELECT * FROM Cart WHERE userid = %s AND isbn = %s"
    cursor.execute(query, (member_id, isbn))
    book = cursor.fetchone()

    if book:
        # If the book is already in the cart, update the quantity
        new_quantity = book[2] + quantity
        query = "UPDATE Cart SET qty = %s WHERE userid = %s AND isbn = %s"
        cursor.execute(query, (new_quantity, member_id, isbn))
    else:
        # If the book is not in the cart, add it
        query = "INSERT INTO Cart (userid, isbn, qty) VALUES (%s, %s, %s)"
        cursor.execute(query, (member_id, isbn, quantity))
    
    conn.commit()
    cursor.close()
    conn.close()
    