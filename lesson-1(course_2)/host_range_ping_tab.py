"""
coding=utf-8
3. Написать функцию host_range_ping_tab(), возможности которой основаны на функции из примера 2.
Но в данном случае результат должен быть итоговым по всем ip-адресам, представленным в табличном формате
(использовать модуль tabulate). Таблица должна состоять из двух колонок и выглядеть примерно так:
Reachable
10.0.0.1
10.0.0.2

Unreachable
10.0.0.3
10.0.0.4
"""
from pprint import pprint
from tabulate import tabulate
from host_range_ping import host_range_ping


def host_range_ping_tab(ping_result=[]):
    if not ping_result:
        ping_result = host_range_ping()
    result = {'Reachable': [], "Unreachable": []}
    # Входной список [('ip_address', Доступность)] преобразуем в словарь,
    # где для удобства отображения отделяем доступные адреса от не доступных
    for item in ping_result:
        if item[1]:
            result["Reachable"].append(item[0])
        else:
            result["Unreachable"].append(item[0])
    print(tabulate(result, headers='keys', tablefmt='pipe'))


if __name__ == "__main__":
    test_ping_result = [
        ('127.0.0.1', True),
        ('127.0.0.2', False),
        ('127.0.0.34', True),
        ('127.0.0.144', False),
        ('127.0.0.255', False),
    ]
    # host_range_ping_tab(test_ping_result)
    host_range_ping_tab()
