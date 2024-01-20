# ✔ Напишите функцию, которая заполняет файл(добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции

from random import randint, uniform


def generate_numbers(file_name: str, amount: int, min_value: int = -1000, max_value: int = 1000):
    with open(file_name, 'w', encoding='utf-8') as f:
        for _ in range(amount):
            f.write(f"{randint(min_value, max_value)}|{round(uniform(min_value, max_value), 2)}\n")
