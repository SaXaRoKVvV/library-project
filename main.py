from loader import load_books
from show_all import show_all
from show_author import show_author
from show_year import show_year
from add_book import add_book
from delete_book import delete_book
from change_copies import change_copies
from input_utils import get_int, get_text
from compare_all import compare_all
from compare_author import compare_author
from compare_year import compare_year

def main():
    books = load_books("books.txt")
    if not books:
        print("База книг пуста или повреждена")
        return

    while True:
        print("=" * 60)
        print("Программа 'Библиотека'")
        print("#" * 60)

        print("МЕНЮ")
        print("1 — Все книги")
        print("2 — По автору")
        print("3 — По году")
        print("4 — Редактирование базы")
        print("0 — Выход")
        print("#" * 60)

        choice = input("Выбор: ").strip()
        if not choice:
            continue

        if choice == "0":
            print("Работа завершена")
            break

        if choice == "1":
            show_all(books, compare_all)
            input("\nEnter — в меню")
            continue

        if choice == "2":
            author = get_text("Автор (0 — назад): ")
            if author == "0":
                continue
            filtered = [book for book in books if book.author == author]
            if filtered:
                show_author(filtered, compare_author)
            else:
                print("Автор не найден")
            input("\nEnter — в меню")
            continue

        if choice == "3":
            start_year = get_int("Начальный год (0 — назад): ")
            if start_year == 0:
                continue
            end_year = get_int("Конечный год (0 — назад): ", start_year)
            if end_year == 0:
                continue
            filtered = [book for book in books if start_year <= book.year <= end_year]
            if filtered:
                show_year(filtered, compare_year, start_year, end_year)
            else:
                print("Книг за период нет")
            input("\nEnter — в меню")
            continue

        if choice == "4":
            while True:
                print("#" * 60)
                print("\nРЕДАКТИРОВАНИЕ БАЗЫ")
                print("1 — Добавить книгу")
                print("2 — Удалить книгу")
                print("3 — Изменить количество экземпляров")
                print("0 — Назад")
                print("#" * 60)

                sub_choice = input("Выбор: ").strip()
                if not sub_choice:
                    continue

                if sub_choice == "0":
                    break
                if sub_choice == "1":
                    add_book(books)
                elif sub_choice == "2":
                    delete_book(books)
                elif sub_choice == "3":
                    change_copies(books)
                else:
                    print("Ошибка: неверный пункт меню")
            continue

        print("Ошибка: неверный пункт меню")

if __name__ == "__main__":
    main()

