"""
Файлы

Файлы открываются функцией open( file_name, mode ). Функция возвращает объект.

file_name - [путь до файла]имя файла

mode - режим работы с файлом:

    'r': только чтение (default)
    'w': запись ”с нуля” (содержимое файла будет стерто)
    'x': создать (если файл существует, будет выброшено исключение)
    'a': запись в конец файла

У объекта file есть следующие функции:

    read(size) - прочитать содержимое файла размером size байтов/символов
    readline() - прочитать строку и передвинуть указатель на следующую
    readlines() - прочитать весь файл и вернуть в виде списка строк
    write() - запись в файл, функция возвращает количество записанных символов
    writelines() - запись в файл списка строк

! Файл закрывается функцией close().

!! Рекомендуется использовать конструкцию with ... as ...:
   так как он закрывает файл автоматически, после отработки блока with ... as
"""

# Пример 1
# f = open('C:\\Course\\file4test.txt', 'w', encoding='utf-8')
# f = open('C:\\Course\\file4test.txt', 'w')  # можно и без кодировки
# for _ in range(10):
#     f.write('5 ')
#     # Чтобы перейти на новую строку,
#     # мы должны явно указать символ новой строки(\n)
#     f.write('Hello world!\n')
# f.writelines(['Вторая', 'строка'])
# f.close()
# #
# # ## Менеджер контекста закрывает файл сам
# with open('C:\\Course\\file4test.txt', encoding='utf-8') as input_file:
# with open('C:\\Course\\file4test.txt') as in_file:
#     for line in in_file.readlines():
#         print(repr(line))  # repr показывает значение как есть

# print()
# print('done')
# Файл уже закрыт!
# in_file.write('hello')  # ValueError: I/O operation on closed file
# #
# ## Считываем без менеджера контекста
# file = open('C:\\Course\\file4test.txt', 'r')
# res = file.readline()  # Считываю первую строку
# while res:
#     print(res, end='')
#     res = file.readline()
# print()
# # Не забываем закрывать файл
# file.close()
# #
# #
# # ## Вариант, который указан выше, с помощью моржового оператора
# # ## Считываем без менеджера контекста
# file = open('C:\\Course\\file4test.txt', 'r')
# while res := file.readline():
#     print(res, end='')
# print()
# # Не забываем закрывать файл
# file.close()

#
# Используем функцию print с файловым идентификатором
file_out = open('C:\\Course\\examples_file.txt', 'w')
print('Hello Python', file=file_out)
print(5, 8, 8.1, file=file_out)
print([45, 23, 23], file=file_out)
print(*[45, 23, 23], file=file_out)
file_out.close()

# # #
# # Путь, как отдельная переменная
path = 'C:\\Course\\examples_file.txt'
# # ## Пример работы менеджера контекста
with open(path) as read_file:
    all_strings = read_file.readlines()

print(all_strings)
for line in all_strings:
    print(line, end='')