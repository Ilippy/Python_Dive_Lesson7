# ✔ Напишите функцию, которая заполняет файл(добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции
def task1(file_name: str, amount: int):
    from task1_generate_numbers import generate_numbers
    generate_numbers(file_name, amount)


# ✔ Напишите функцию, которая генерирует псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.
def task2(file_name: str, amount: int):
    from task2_generate_names import generate_names
    generate_names(file_name, amount)


# ✔ Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните имя и произведение:
#   * если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
#   * если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк, сколько в более длинном файле.
# ✔ При достижении конца более короткого файла, возвращайтесь в его начало.
def task3(file_numbers, file_names, file_numbers_and_names):
    from task3_generate_numbers_names import generate_numbers_names
    generate_numbers_names(file_numbers, file_names, file_numbers_and_names)


# ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
#   * расширение
#   * минимальная длина случайно сгенерированного имени, по умолчанию 6
#   * максимальная длина случайно сгенерированного имени, по умолчанию 30
#   * минимальное число случайных байт, записанных в файл, по умолчанию 256
#   * максимальное число случайных байт, записанных в файл, по умолчанию 4096
#   * количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.
def task4(extension: str, min_len_name=6, max_len_name=30, min_byte=256, max_byte=4096, files_amount=42):
    from task4_generate_files import generate_files
    generate_files(extension, min_len_name, max_len_name, min_byte, max_byte, files_amount)


# Доработаем предыдущую задачу.
# Создайте новую функцию которая генерирует файлы с разными расширениями.
# Расширения и количество файлов функция принимает в качестве параметров.
# Количество переданных расширений может быть любым. Количество файлов для каждого расширения различно.
# Внутри используйте вызов функции из прошлой задачи.
def task5(lst_extensions: list, amount_of_files):
    from task5_generate_files import create_files_with_extension
    create_files_with_extension(lst_extensions, amount_of_files)


# Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# Каждая группа включает файлы с несколькими расширениями.
# В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
def task6(lst_extensions, amount_of_files):
    from task6_generate_files import create_files_with_extension
    create_files_with_extension(lst_extensions, amount_of_files)


def main():
    file_numbers = 'numbers.txt'
    file_names = 'names.txt'
    file_numbers_and_names = 'names_and_numbers.txt'
    extensions = ['img', 'png', 'jpeg', 'gif', 'doc', 'txt', 'raf', 'docx']
    # task1(file_numbers, 5)
    # task2(file_names, 7)
    # task3(file_numbers, file_names, file_numbers_and_names)
    # task4('txt')
    # task5(extensions, 10)
    task6(extensions, 15)


if __name__ == '__main__':
    main()
