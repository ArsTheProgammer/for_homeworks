import random
from random import randint

'''
Напишите функцию, которая принимает список чисел и
возвращает наибольшее из них.
'''
lst_new = [randint(1, 100) for _ in range(15)]


# print(lst_new)


def get_max_num():
    return max(lst_new)


# print(get_max_num())

"""100, два раза выдало макс значение рандинт !!!!!!!!!!!!!!!!!!!!!!!"""

'''
Напишите функцию, которая принимает список строк и возвращает новый список строк,
в котором каждый элемент написан заглавными буквами.
'''


def titling(lst: list):
    new_lst = []
    for sentence in lst:
        string_quote = str(sentence)
        new_quote = string_quote.title()
        new_lst.append(new_quote)
    return new_lst


# print(titling(["Напишите функцию, которая принимает", "написан заглавными буквами"]))

'''
Задача на создание списка из четных чисел от 1 до 100: создать список,
содержащий все четные числа от 1 до 100.
'''
# print([i for i in range(1, 101) if i % 2 == 0])
'''
Задача на создание списка из элементов, 
которые находятся только в одном из двух списков: 
создать список, содержащий все элементы, 
которые находятся только в списке A или только в списке B.'''

list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]
lst_a = list_a[:]
lst_a.extend(list_b)
# print(lst_a)
for i in lst_a:
    counter = lst_a.count(i)
    if counter > 1:
        lst_a.remove(i)
# print(lst_a)

list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]
lst_a = list_a[:]
lst_a.extend(list_b)
# print(list(set(lst_a)))

'''
Напишите функцию, которая принимает список строк и возвращает новый список,
содержащий только строки, которые начинаются с заданной подстроки.
'''


def find_unique_string(lst: list, phrase: str):
    lst_sorted = []
    for sentence in lst:
        string_quote = str(sentence)
        if string_quote.startswith(phrase):
            lst_sorted.append(string_quote)
        else:
            lst_sorted.append(None)
    return lst_sorted


print(find_unique_string(["строку и возвращает новую", "строку, в которой каждое слово", "Напиш"], "троку"))

'''
Напишите функцию, которая принимает строку и возвращает новую строку,
в которой каждое слово написано задом наперед.
'''
