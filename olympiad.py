# Cделать возможность пользователю ввести параметры отправляемого груза,
# такие как длинна, ширина, высота, масса.
# каждый ввод пользователя раскидывать по двум спискам,
# в первом списке будет произведение всех трех измерений, образуя тем самым , во втором масса посылки.
# расчитать возможность пересылки данного груза в зависимости от вместимости
# контейнера(размеры из интернета)
# в случае если параметры груза позволяют отправить его в контейнере, вывести сообщение об этом,
# если нет таковой возможности, сообщить об излишке после наполнения контейнера.


""" Параметры контейнера - 42,5 х 26,5 х 38 """

# import barcode_creation
from prettytable import PrettyTable
# import pathlib
# from pathlib import Path


class PackageLable:

    def __init__(self, number=0, sum_of_all=0, odd=0):
        self.number = number
        self.sum_of_all = sum_of_all
        self.odd = odd

    def __str__(self):
        return f'номер : {self.number}, объём : {self.sum_of_all}, ' f'масса : {self.odd}'

    #    def create_params(self):
    #        parcel_params = [self.number, self.sum_of_all, self.odd]
    #        for i in range(len(parcel_params)):
    #            parcel_params[i] = int(parcel_params[i])

    def create_tables(self, a):
        x = PrettyTable()
        x.field_names = ["Номер", "Объём", "Вес", "Штрих - код"]
        x.add_row([f"{self.number}", f"{self.sum_of_all} cm^3", f"{self.odd} kg", f"blank temporarly"])

        print(x)

        file_out = open(f"{a}", 'a', encoding='utf-8')
        print(x, file=file_out)
        file_out.close()


oz = PackageLable(1, 457, 45)
# oz.create_params()
oz.create_tables('C:\\Users\\Михаил\\Desktop\\Арсений\\питон\\parcel_info.txt')
