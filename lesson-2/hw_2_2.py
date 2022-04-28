"""
coding=utf-8
Есть файл orders в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий его заполнение данными.
 Для этого:
Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity),
цена (price), покупатель (buyer), дата (date). Функция должна предусматривать запись данных в виде словаря
в файл orders.json. При записи данных указать величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.
"""
import json


def write_order_to_json(item, quantity, price, buyer, date):
    """write to  json-file"""
    order_to_dump = {
        'item': item,
        'quantity': quantity,
        'price': price,
        'buyer': buyer,
        'date': date,
    }

    with open('orders.json', 'r', encoding='utf-8') as f_n:
        obj = json.load(f_n)

    obj['orders'].append(order_to_dump)

    with open('orders.json', 'w', encoding='utf-8') as f_n:
        json.dump(obj, f_n, ensure_ascii=False, indent=4)


order_example = [
    {
        'item': 'item1',
        'quantity': 10,
        'price': 2.5,
        'buyer': 'buyer',
        'date': '10.01.2012',
    },
    {
        'item': 'item2',
        'quantity': 15,
        'price': 2.8,
        'buyer': 'buyer2',
        'date': '10.02.2012',
    }
]

item_1 = order_example[0]
item_2 = order_example[1]
write_order_to_json(item_1['item'], item_1['quantity'], item_1['price'], item_1['buyer'], item_1['date'])
write_order_to_json(item_2['item'], item_2['quantity'], item_2['price'], item_2['buyer'], item_2['date'])
