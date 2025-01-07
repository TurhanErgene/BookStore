from services.book import get_books_by_subject

def browse_by_subject(subject):
    books = get_books_by_subject(subject)
    # Logic to paginate and display books
    return books

def search_by_author(search):
    # Logic to search by author/title
    pass

def search_by_title(search):
    # Logic to search by author/title
    pass 