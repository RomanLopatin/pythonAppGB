"""
coding=utf-8
2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в
последовательность кодов (не используя методы encode, decode или функцию bytes) и определить тип,
содержимое и длину соответствующих переменных.
"""


# def create_bytes_repr_bak(my_list):
#     """returns bytes repr of array"""
#     return [bytes(item, encoding='utf-8') for item in my_list]


def create_bytes_repr(my_list):
    """returns bytes repr of ascii array"""
    return [eval(f"b'{item}'") for item in my_list]


def print_item_list_info(my_list):
    """Печатает инфо (тип, содержание и длину) об элементах списка"""
    for item in my_list:
        print('type:', type(item), ', repr:', item, ', len:', len(item))


WORD_LIST_LAT = [
    'class',
    'function',
    'method',
]

WORD_LIST_BYTES = create_bytes_repr(WORD_LIST_LAT)
print_item_list_info(WORD_LIST_BYTES)
