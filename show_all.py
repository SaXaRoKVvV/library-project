from heap_sort import heap_sort
from print_table import print_books_table

def show_all(books, compare):
    """Вывод полного списка книг с сортировкой."""
    heap_sort(books, compare)
    print("#" * 95)
    print("ВСЕ КНИГИ")
    print_books_table(books)
    print("#" * 95)
