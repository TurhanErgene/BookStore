from config.database import get_connection


def check_cart(member_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM Cart WHERE userid = %s"
    cursor.execute(query, (member_id,))
    cart = cursor.fetchall()
    cursor.close()
    conn.close()
    return cart


def checkout(member_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    
    # Fetch cart items for the user
    query = "SELECT * FROM Cart WHERE userid = %s"
    cursor.execute(query, (member_id,))
    cart = cursor.fetchall()
    
    if not cart:
        print("\nYour cart is empty.")
        cursor.close()
        conn.close()
        return

    print("=" * 60)
    print("\nYour cart:")
    total = 0
    order_items = []  # To hold the order details for insertion

    for item in cart:
        isbn = item['isbn']
        quantity = item['qty']

        # Find book details by ISBN
        book = find_book_by_isbn(isbn)
        if not book:
            print(f"Book with ISBN {isbn} not found. Skipping...")
            continue

        title = book['title']
        price = book['price']
        subtotal = price * quantity
        total += subtotal

        print(f"\nTitle: {title}")
        print(f"ISBN: {isbn}")
        print(f"Price: ${price:.2f}")
        print(f"Quantity: {quantity}")
        print(f"Subtotal: ${subtotal:.2f}")

        # Prepare order detail data (without `userid`)
        order_items.append((isbn, quantity, subtotal))

    print("\nTotal: ${:.2f}".format(total))
    print("=" * 60)
    print("\nChecking out...")

    # Insert into orderdetails
    for item in order_items:
        query = "INSERT INTO orderdetails (isbn, qty, amount) VALUES (%s, %s, %s)"
        cursor.execute(query, item)  # Ensure item matches the placeholders

    # Clear the cart
    query = "DELETE FROM Cart WHERE userid = %s"
    cursor.execute(query, (member_id,))

    conn.commit()
    cursor.close()
    conn.close()
    print("\nCheckout successful! Your cart has been cleared.")



def find_book_by_isbn(isbn):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM Books WHERE isbn = %s"
    cursor.execute(query, (isbn,))
    book = cursor.fetchone()
    cursor.close()
    conn.close()
    return book
