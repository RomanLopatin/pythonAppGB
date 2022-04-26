"""
coding=utf-8
Преобразовать слова «разработка», «администрирование», «protocol», «standard» из
строкового представления в байтовое и выполнить обратное преобразование (используя
методы encode и decode).
"""
CODING_TYPE = 'utf-8'

def convert_string_to_bytes(my_list, coding):
    """converts string to bytes"""
    return [item.encode(coding) for item in my_list]


def convert_bytes_to_string(my_list, coding):
    """converts bytes to string  """
    return [item.decode(coding) for item in my_list]


def print_item_list(my_list):
    """Prints list elements"""
    for item in my_list:
        print(item)


WORD_LIST = [
    'разработка',
    'администрирование',
    'protocol',
    'standard',
]

WORD_LIST_BYTES = convert_string_to_bytes(WORD_LIST, CODING_TYPE)
print_item_list(WORD_LIST_BYTES)

WORD_LIST_STRING = convert_bytes_to_string(WORD_LIST_BYTES, CODING_TYPE)
print_item_list(WORD_LIST_STRING)
