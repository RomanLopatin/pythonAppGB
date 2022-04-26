"""
coding=utf-8
3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в
байтовом типе.
"""


def bytes_conversion_error_print(my_list):
    """ выводит слово, если невозможно записать в байтовом типе """
    for item in my_list:
        item_byte_repr = item.encode('ascii', 'ignore')
        if len(item_byte_repr) != len(item):
            print(item, " - ошибка приведения к байтовому типу!")


WORD_LIST = [
    'attribute',
    'класс',
    'функция',
    'type',
]

bytes_conversion_error_print(WORD_LIST)
