import db_price_list
from db_price_list import price_dict
import pprint as pp

"""Напишите класс "Заказ", который содержит следующие атрибуты:

Номер заказа
Список товаров в заказе
Общая стоимость заказа
Дата оформления заказа
Класс должен иметь следующие методы:

"добавить товар": добавляет товар в список товаров в заказе "удалить товар": удаляет товар из списка товаров в заказе 
"рассчитать стоимость заказа": пересчитывает общую стоимость заказа на основе списка товаров в заказе "показать 
информацию о заказе": выводит на экран информацию о заказе, включая номер заказа, список товаров в заказе, 
общую стоимость заказа и дату оформления заказа """


class Order:

    def __init__(self, order_number=0, date=''):
        self.price = 0
        self.list_of_items = []
        self.order_number = order_number
        self.date = date

    def show_price(self):
        return self.price

    def add_item(self, purchase, cost):
        self.list_of_items.append((purchase, cost))
        self.price += cost
        return "Your item is successfully added"

    def show_info(self):
        return f"{self.list_of_items}, {self.order_number}, {self.date}"

    def show_prices(self):
        list_of_prices = []
        for key, values in db_price_list.price_dict.items():
            list_of_prices.append((f"{key} - {values}"))
        return list_of_prices
        # десериализатор

    def delete_item(self, item):
        for element in self.list_of_items:
            if element[0] == item:
                self.list_of_items.pop(self.list_of_items.index(element))
        return self.list_of_items


order = Order(231, "23/02/2023")
print(order.add_item("boots", 3000))
print(order.show_info())
print(order.add_item("shirt", 2500))
print(order.show_info())
print(order.delete_item("shirt"))
print(order.show_info())
print(order.show_price())

















"""class Order:
    def __init__(self, order_number, date):
        self.order_number = order_number
        self.items = []
        self.total_cost = 0
        self.date = date

    def add_item(self, item, price):
        self.items.append((item, price))
        self.total_cost += price

    def remove_item(self, item):
        for i in range(len(self.items)):
            if self.items[i][0] == item:
                self.total_cost -= self.items[i][1]
                del self.items[i]
                break

    def calculate_total_cost(self):
        self.total_cost = sum(item[1] for item in self.items)

    def show_order_info(self):
        print(f"Order number: {self.order_number}")
        print("Items:")
        for item, price in self.items:
            print(f"- {item}: ${price}")
        print(f"Total cost: ${self.total_cost}")
        print(f"Date: {self.date}")"""
