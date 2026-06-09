from input_utils import get_text
from save_books import save_books
from print_table import print_books_table


def delete_book(books):
    """Удаляет книгу по названию и сохраняет изменения."""
    print("#" * 50)
    print("УДАЛЕНИЕ КНИГИ")
    print("#" * 50)

    print("\nТекущий список книг:")
    print_books_table(books)

    title = get_text("Название книги (0 — назад): ")
    if title == "0":
        return

    for book in books:
        if book.title.lower() == title.lower():
            books.remove(book)
            save_books(books)
            print("Книга удалена")
            return

    print("Книга не найдена")


