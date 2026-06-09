def compare_author(book1, book2):
    """Сравнивает книги одного автора: издательство↓, название↑."""
    if book1.publisher != book2.publisher:
        return book1.publisher < book2.publisher
    return book1.title > book2.title
