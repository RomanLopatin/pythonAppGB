"""
coding=utf-8
П5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из
байтовового в строковый тип на кириллице.
"""

import chardet  # необходима предварительная инсталляция: pip install chardet
import subprocess
import platform


def url_ping_info(url):
    """ get url ping info """
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    args = ['ping', param, '2', url]
    process = subprocess.Popen(args, stdout=subprocess.PIPE)
    print('*' * 70)
    for line in process.stdout:
        result = chardet.detect(line)
        result_encoding = result['encoding']

        line_decode = line.decode(result_encoding)
        print(line_decode)


url_list = [
    'yandex.ru',
    'youtube.com',
]

for url_item in url_list:
    url_ping_info(url_item)
