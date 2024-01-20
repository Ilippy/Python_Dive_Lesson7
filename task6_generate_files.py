# Доработаем предыдущую задачу.
# Создайте новую функцию которая генерирует файлы с разными расширениями.
# Расширения и количество файлов функция принимает в качестве параметров.
# Количество переданных расширений может быть любым. Количество файлов для каждого расширения различно.
# Внутри используйте вызов функции из прошлой задачи.

from string import ascii_lowercase
from random import choice, randint
from pathlib import Path

EXTENSIONS = {
    Path(Path.cwd() / "img"): ['img', 'png', 'jpeg', 'gif'],
    Path(Path.cwd() / "text"): ['doc', 'txt', 'raf', 'docx']
}


def _generate_name(min_len_name, max_len_name, extension):
    name = ''
    for _ in range(randint(min_len_name, max_len_name)):
        name += choice(ascii_lowercase)
    return f"{name}.{extension}"


def generate_file(extension: str, folder: Path, min_len_name=6, max_len_name=30, min_byte=256, max_byte=4096):
    while True:
        file = Path(folder / _generate_name(min_len_name, max_len_name, extension))
        if not file.exists():
            with open(file, 'wb') as file:
                file.write(bytes(randint(min_byte, max_byte)))
                return


def create_files_with_extension(lst_extensions: list, amount_of_files):
    for _ in range(amount_of_files):
        extension = choice(lst_extensions)
        for path, extensions in EXTENSIONS.items():
            if extension in extensions:
                path.mkdir(exist_ok=True)
                generate_file(extension, path)
                break
