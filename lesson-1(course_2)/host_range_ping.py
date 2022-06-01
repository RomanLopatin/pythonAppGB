"""
coding=utf-8
2.
Написать функцию host_range_ping() для перебора ip-адресов из заданного диапазона.
Меняться должен только последний октет каждого адреса. По результатам проверки должно
выводиться соответствующее сообщение
"""
from ipaddress import ip_address
from pprint import pprint

from host_ping import host_ping


def host_range_ping():

    while True:
        start_ip_str = input("Введите стартовый ip-адрес: ")
        try:
            start_ip_ipv4 = ip_address(start_ip_str)
            last_octet = int(start_ip_str.split('.')[3])
            break
        except Exception as e:
            print(e)

    while True:
        max_ip_num = 255 + 1 - last_octet
        stop_ip_str = input(f"Сколько адресов проверить? (число от 1 до {max_ip_num}): ")
        if not stop_ip_str.isnumeric() or int(stop_ip_str) == 0:
            print(f"Необходимо ввести целое число от 1 до {max_ip_num}")
        else:
            stop_ip_num = int(stop_ip_str)
            if stop_ip_num > max_ip_num:
                print(f"Вышли за пределы октета!")
            else:
                break
    host_list = []
    [host_list.append(str(start_ip_ipv4 + ind)) for ind in range(stop_ip_num)]

    return host_ping(host_list)


if __name__ == "__main__":
    pprint(host_range_ping())
