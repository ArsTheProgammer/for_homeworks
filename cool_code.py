
def sorter():
    list_a = [1, 2, 3, 4, 5]
    list_b = [4, 5, 6, 7, 8]
    lst_a = list_a[:]
    lst_a.extend(list_b)
    print(lst_a)
    for i in lst_a:
        counter = lst_a.count(i)
        if counter > 1:
            lst_a.remove(i)
    print(lst_a)


def sorter_new():
    list_a = [1, 2, 3, 4, 5]
    list_b = [4, 5, 6, 7, 8]
    lst_a = list_a[:]
    lst_a.extend(list_b)
    print(list(set(lst_a)))