"""
coding=utf-8
1.
Написать функцию host_ping(), в которой с помощью утилиты ping будет проверяться доступность сетевых узлов.
Аргументом функции является список, в котором каждый сетевой узел должен быть представлен именем хоста или ip-адресом.
В функции необходимо перебирать ip-адреса и проверять их доступность с выводом соответствующего сообщения
(«Узел доступен», «Узел недоступен»). При этом ip-адрес сетевого узла должен создаваться с помощью функции ip_address().
 (Внимание! Аргументом сабпроцеса должен быть список, а не строка!!! Для уменьшения времени работы скрипта при проверке
 нескольких ip-адресов, решение необходимо выполнить с помощью потоков)
"""
from threading import Thread
from ipaddress import ip_address
import subprocess
import platform
from pprint import pprint


def ping_ip_address(ipv4, res):
    """ get ping result """

    param = '-n' if platform.system().lower() == 'windows' else '-c'
    host_addr_str = str(ipv4)
    args = ['ping', param, '1', host_addr_str]
    ping_reply = subprocess.Popen(args, stdout=subprocess.PIPE)
    code = ping_reply.wait()
    res.append((host_addr_str, code == 0))


def host_ping(host_list):
    """ get host_list ping result, uses threads """
    thread_list = []
    result = []

    for host_item in host_list:
        try:
            host_item_ipv4 = ip_address(host_item)
        except ValueError as e:
            host_item_ipv4 = host_item  # значит это доменное имя
        thread_item = Thread(target=ping_ip_address, args=(host_item_ipv4, result), daemon=True)
        thread_item.start()
        thread_list.append(thread_item)

    [thread_item.join() for thread_item in thread_list]

    return result


if __name__ == '__main__':
    test_host_list = [
        'yandex.ru',
        'yandx.ru',
        'bbc.com',
        'youtube.com',
        'facebook.com',
        'instagram.com',
        '192.168.0.1',
        '127.0.0.1',
    ]

    res = host_ping(test_host_list)
    pprint(res)
