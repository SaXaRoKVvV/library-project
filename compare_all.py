def compare_all(book1, book2):
    """Сравнивает книги для полного списка: автор↑, год↓, экземпляры↓."""
    if book1.author != book2.author:
        return book1.author > book2.author
    if book1.year != book2.year:
        return book1.year < book2.year
    return book1.copies < book2.copies
