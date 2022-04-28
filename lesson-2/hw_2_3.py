"""
coding=utf-8
Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом, отсутствующим
в кодировке ASCII (например, €);
Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml. При этом обеспечить стилизацию файла
с помощью параметра default_flow_style, а также установить возможность работы с юникодом: allow_unicode = True;
Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.
"""
import yaml

data_to_write = {
    'key1': ['a', 'b', 'c'],
    'key2': 777,
    'key3': {
        'key3_1': '10€',
        'key3_2': '$15',
        'key3_3': '10₽',
    }
}

with open('file.yaml', 'w', encoding='utf-8') as f_n:
    yaml.dump(data_to_write, f_n, default_flow_style=False, allow_unicode=True)

with open('file.yaml', encoding='utf-8') as f_n:
    f_n_content = yaml.load(f_n, Loader=yaml.FullLoader)

print("Equal data? ", data_to_write == f_n_content)
