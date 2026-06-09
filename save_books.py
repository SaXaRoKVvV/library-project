def save_books(books, filename="books.txt"):
    """Сохраняет текущую базу книг в файл в исходном формате."""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            for book in books:
                line = f"{book.author};{book.title};{book.publisher};{book.year};{book.pages};{book.copies}\n"
                f.write(line)
    except Exception as e:
        print(f"Ошибка при сохранении файла: {e}")