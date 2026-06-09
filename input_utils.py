def get_int(prompt, min_value=None):
    """Ввод целого числа с проверкой на отрицательные значения и минимальное значение."""
    while True:
        try:
            value = int(input(prompt).strip())
            if value < 0:
                print("Ошибка: значение не может быть отрицательным")
                print("#" * 60)
                continue
            if min_value is not None and value < min_value:
                print("Ошибка: значение слишком маленькое")
            else:
                return value
        except ValueError:
            print("Ошибка: введите целое число")


def get_text(prompt):
    """Ввод непустой строки."""
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("Ошибка: строка не должна быть пустой")
