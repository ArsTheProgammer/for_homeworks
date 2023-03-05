'''
Описание: Класс, представляющий человека с именем,
возрастом и местом жительства.
Пропишите документацию к классу и загрузите готовый проtкт на GitHub

Конструктор:

__init__(self, name: str, age: int, city: str) - инициализирует объект класса Person
с заданным именем, возрастом и местом жительства.
Методы:

get_name(self) -> str - возвращает имя человека.
get_age(self) -> int - возвращает возраст человека.
get_city(self) -> str - возвращает место жительства человека.
'''


class Student:
    """
        Этот класс представляет объект человека.

        Атрибуты:
            name (str): Имя человека.
            age (int): Возраст человека.
            city (str): Город, где живет человек.
        """

    # """a class to return all info about the student"""
    def __init__(self, name: str, age: int, city: str):
        self.name = name
        self.age = age
        self.city = city

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_city(self):
        return self.city


"""stud_1 = Student("Ivan", 21, "Moscow")
print(stud_1.get_name())
print(stud_1.get_age())
print(stud_1.get_city())
print(stud_1.__doc__)
"""

'''
Напишите функцию, которая принимает 
список чисел и возвращает сумму всех чисел в списке.
'''


def sum_of_all(a):
    summon = 0
    for i in a:
        summon += i
    return f"сумма всех элементов - {summon}"


# print(sum_of_all([8, 12, 4, 17, 6, 21, 3, 14]))

'''
Напишите функцию, которая принимает два аргумента: 
строку и символ. Функция должна вернуть количество раз, 
которое символ встречается в строке.
'''


def find_unique_quantity(a: str, b: str):
    lst_a = list(a)
    object_quantity = lst_a.count(b)
    return f"кол-во вхождений символа {b} в строку {a} - {object_quantity}"


# print(find_unique_quantity("hfudhfdlshgdhgkhdgh", "h"))

'''
Подсчет частотности элементов в списке.

my_list = ['apple', 'banana', 'banana', 'cherry', 'cherry', 'cherry']

Допустим, у нас есть список, и мы хотим посчитать, 
сколько раз каждый элемент встречается в этом списке. 
Мы можем использовать словарь, чтобы сохранить эти результаты. 
'''
"""my_lst = ['apple', 'banana', 'banana', 'cherry', 'cherry', 'cherry']
cherries = my_lst.count("cherry")
apples = my_lst.count("apple")
bananas = my_lst.count("banana")
new_string = F"{apples}{bananas}{cherries}"
lst_string = list(new_string)
# print(lst_string)
my_new_lst = my_lst[:]
for i in range(len(my_new_lst)):
    counter = my_new_lst.count(i)
    if counter > 1:
        idexer = my_new_lst.index(i)
        srez = my_new_lst[idexer:counter - 1]
        my_new_lst.remove(srez)
        break
dictionary = dict(zip(my_new_lst, lst_string))
print(dictionary)"""
my_lst_tmp = ['apple', 'banana', 'banana', 'cherry', 'cherry', 'cherry']
new_dict = {}
for fruit in my_lst_tmp:
    if not fruit in new_dict:
        new_dict[f"{fruit}"] = 1
    else:
        new_dict[f"{fruit}"] += 1
print(new_dict)
'''
Фильтрация элементов в списке по условию

my_list = [8, 12, 4, 17, 6, 21, 3, 14]

Допустим, у нас есть список чисел, и мы хотим оставить только те числа, 
которые больше 10. Мы можем использовать цикл для прохождения по списку 
и условный оператор if, чтобы проверить каждый элемент.'''

my_list = [8, 12, 4, 17, 6, 21, 3, 14]
my_list_new = []
for j in my_list:
    if j > 10:
        my_list_new.append(j)

# print(f"отсортированый список - {my_list_new}")
