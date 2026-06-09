def print_books_table(books):
    """
    Вывод списка книг в виде таблицы без копирования списка.
    Колонки: Автор | Название | Издатель | Год | Стр. | Экземпляры
    """
    # Заголовки
    print(f"{'Автор':20} | {'Название':30} | {'Издатель':20} | {'Год':4} | {'Стр.':5} | {'Экз.':5}")
    print("-" * 95)

    # Строки с книгами
    for book in books:
        print(f"{book.author:20} | {book.title:30} | {book.publisher:20} | {book.year:4} | {book.pages:5} | {book.copies:5}")
    print("#" * 95)