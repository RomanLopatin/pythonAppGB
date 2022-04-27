"""
coding=utf-8
Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое
программирование», «сокет», «декоратор». Проверить кодировку файла по умолчанию.
Принудительно открыть файл в формате Unicode и вывести его содержимое.
"""

from chardet import detect


def get_file_content(file_name):
    """получаем содержимое файла"""
    encoding = None
    try:
        with open(file_name, 'rb') as f_obj:
            content_bytes = f_obj.read()
            encoding = detect(content_bytes)['encoding']
            return content_bytes.decode(encoding)

    except IOError:
        print("Произошла ошибка ввода-вывода!")


FILE_NAME = "test_file.txt"
print(get_file_content(FILE_NAME))
