from Book import Book
from input_utils import get_int, get_text
from save_books import save_books

def add_book(books):
    """Добавляет новую книгу в базу и сохраняет изменения."""
    print("#" * 50)
    print("ДОБАВЛЕНИЕ КНИГИ")
    print("#" * 50)

    author = get_text("Автор: ")
    title = get_text("Название: ")
    publisher = get_text("Издательство: ")
    year = get_int("Год выпуска: ")
    pages = get_int("Количество страниц: ", 1)
    copies = get_int("Количество экземпляров: ", 0)

    book = Book(author, title, publisher, year, pages, copies)
    books.append(book)

    save_books(books)
    print("Книга успешно добавлена")