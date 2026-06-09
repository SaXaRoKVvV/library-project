from input_utils import get_int, get_text
from save_books import save_books
from print_table import print_books_table

def change_copies(books):
    """Изменяет количество экземпляров книги и сохраняет изменения."""
    print("#" * 50)
    print("ИЗМЕНЕНИЕ КОЛИЧЕСТВА ЭКЗЕМПЛЯРОВ")
    print("#" * 50)

    print("\nТекущий список книг:")
    print_books_table(books)

    title = get_text("Название книги (0 — назад): ")
    if title == "0":
        return

    for book in books:
        if book.title == title:
            print(f"Текущее количество экземпляров: {book.copies}")
            book.copies = get_int("Новое количество: ", 0)
            save_books(books)
            print("Количество экземпляров обновлено")
            return

    print("Книга не найдена")
