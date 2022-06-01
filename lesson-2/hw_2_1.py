"""
coding=utf-8
Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание данных.
 В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров «Изготовитель
системы», «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра поместить в соответствующий список.
Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list, os_type_list. В этой же функции
создать главный список для хранения данных отчета — например, main_data — и поместить в него названия столбцов отчета
в виде списка: «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения для этих столбцов также
оформить в виде списка и поместить в файл main_data (также для каждого файла);
Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение данных
через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;
Проверить работу программы через вызов функции write_to_csv()
"""
import csv

from chardet import detect
import re


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


def get_data():
    """get data from csv-file"""
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = []

    file_list = [
        "info_1.txt",
        "info_2.txt",
        "info_3.txt",
    ]

    headers_list = [
        'Изготовитель системы',
        'Название ОС',
        'Код продукта',
        'Тип системы',
    ]

    for file in file_list:
        file_content = get_file_content(file)
        #
        param = re.findall(r'Изготовитель системы:\s+\S+', file_content)[0].split()[2]
        os_prod_list.append(param)
        #
        param = re.findall(r'Название ОС:\s+\S+', file_content)[0].split()[2]
        os_name_list.append(param)
        #
        param = re.findall(r'Код продукта:\s+\S+', file_content)[0].split()[2]
        os_code_list.append(param)
        #
        param = re.findall(r'Тип системы:\s+\S+', file_content)[0].split()[2]
        os_type_list.append(param)

    main_data.append(headers_list)

    for i in range(len(os_prod_list)):
        main_data_str = [os_prod_list[i], os_name_list[i], os_code_list[i], os_type_list[i]]
        main_data.append(main_data_str)

    return main_data


def write_to_csv():
    """write to csv-file"""
    with open('data.csv', 'w', encoding="utf-8", newline='') as f_n:
        data = get_data()
        f_n_writer = csv.writer(f_n)
        f_n_writer.writerows(data)
        # for line in data:
        #     f_n_writer.writerow(line)


write_to_csv()
