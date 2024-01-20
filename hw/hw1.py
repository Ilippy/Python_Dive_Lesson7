# Напишите функцию группового переименования файлов в папке test_folder под названием rename_files. Она должна:

# a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# b. принимать параметр количество цифр в порядковом номере.
# c. принимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# d. принимать параметр расширение конечного файла.
# e. принимать диапазон сохраняемого оригинального имени.
# Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
# f. Папка test_folder доступна из текущей директории

from pathlib import Path


def rename_files(desired_name, num_digits, source_ext, target_ext):
    folder = Path(Path().cwd())
    # new_folder = folder / "test_folder"
    # new_folder.mkdir(exist_ok=True)
    num = 1
    for file in folder.iterdir():
        if file.suffix[1:] == source_ext:
            # print(file)
            file.rename(f"{desired_name}_{num: 0{num_digits}d}.{target_ext}")
            num += 1


if __name__ == '__main__':
    rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc")
