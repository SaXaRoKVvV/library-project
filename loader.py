from Book import Book

def load_books(filename):
    """
    Загрузка книг из файла.
    """
    books = []

    try:
        with open(filename, encoding="utf-8") as file:
            for line_number, line in enumerate(file, 1):
                parts = line.strip().split(";")

                if len(parts) != 6:
                    print(f"Ошибка формата в строке {line_number}")
                    continue

                try:
                    year = int(parts[3])
                    pages = int(parts[4])
                    copies = int(parts[5])

                    book = Book(
                        parts[0],
                        parts[1],
                        parts[2],
                        year,
                        pages,
                        copies
                    )
                    books.append(book)

                except ValueError:
                    print(f"Ошибка числовых данных в строке {line_number}")

    except FileNotFoundError:
        print("Ошибка: файл books.txt не найден")

    return books
