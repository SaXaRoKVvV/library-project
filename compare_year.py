def compare_year(book1, book2):
    """Сравнивает книги по году: год↓, автор↑."""
    if book1.year != book2.year:
        return book1.year < book2.year
    return book1.author > book2.author
