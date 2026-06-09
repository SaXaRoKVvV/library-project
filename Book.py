class Book:
    """
Класс книги.

Атрибуты:
- author: автор книги
- title: название
- publisher: издательство
- year: год выпуска
- pages: количество страниц
- copies: количество экземпляров
    """

    def __init__(self, author, title, publisher, year, pages, copies):
        self.author = author
        self.title = title
        self.publisher = publisher
        self.year = year
        self.pages = pages
        self.copies = copies

    def __str__(self):
        return (
            f"{self.author} | {self.title} | {self.publisher} | "
            f"{self.year} | {self.pages} стр. | {self.copies} экз."
        )
