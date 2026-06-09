from heap_sort import heap_sort
from print_table import print_books_table

def show_author(books, compare):
    """Вывод книг выбранного автора с сортировкой."""
    heap_sort(books, compare)
    print("#" * 95)
    print("КНИГИ ВЫБРАННОГО АВТОРА")
    print_books_table(books)
    print("#" * 95)
