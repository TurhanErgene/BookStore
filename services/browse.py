from models.book import get_books_by_subject

def browse_by_subject(subject):
    books = get_books_by_subject(subject)
    # Logic to paginate and display books
    return books
