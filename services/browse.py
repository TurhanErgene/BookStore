from services.book import get_all_subjects, get_books_by_subject_paginated
from services.cart import add_to_cart


def browse_by_subject(member_id):
    subjects = get_all_subjects()
    if not subjects:
        print("\nNo subjects available.")
        return

    print("\nAll book subjects: ")
    for i, subject in enumerate(subjects, 1):
        print(f"{i}. {subject}")

    # Choose a subject
    choice = input(
        "\nEnter the number corresponding to your choice, or press ENTER to go back: "
    )
    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(subjects):
        print("\nInvalid choice. Please try again.")
        return

    selected_subject = subjects[int(choice) - 1]
    print(f"\nBooks available in the subject: {selected_subject}")

    per_page = 2  # Number of books per page

    while True:
        # Ask user for the page number
        page = input("\nEnter the page number (or press ENTER to go back): ")
        if not page:
            break  # Exit if user presses ENTER
        if not page.isdigit() or int(page) < 1:
            print("\nInvalid page number. Please try again.")
            continue
        

        # Calculate offset based on the page number
        offset = (int(page) - 1) * per_page  # Offset calculation
        # since 

        # Fetch paginated books
        books = get_books_by_subject_paginated(selected_subject, offset, per_page)
        if not books:
            print("\nNo books available on this page.")
            continue

        # Display the books
        for book in books:
            print(
                f"""
                Author: {book['author']}
                Title: {book['title']}
                ISBN: {book['isbn']}
                Price: ${book['price']}
                Subject: {book['subject']}
                """
            )

        # Allow adding books to the cart
        action = input(
            "Enter ISBN to add to Cart, or press ENTER to choose another page: "
        )
        if not action:
            continue
        elif action.isdigit():
            if len(action) != 13:
                print("\nInvalid ISBN. Please try again.")
                continue
            isbn = action
            quantity = int(input("Enter quantity: "))
            add_to_cart(member_id, isbn, quantity)
            print(f"Added ISBN {isbn} with quantity {quantity} to the cart.")
