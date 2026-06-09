from heap_sort import heap_sort
from print_table import print_books_table

def show_year(books, compare, start_year, end_year):
    """Вывод книг за заданный период с сортировкой."""
    heap_sort(books, compare)
    print("#" * 95)
    print(f"КНИГИ ЗА ПЕРИОД {start_year}–{end_year}")
    print_books_table(books)
    print("#" * 95)
