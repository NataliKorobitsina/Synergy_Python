# Урок № 14, задание 1
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def func(x):
    if not x:
        return print('Конец списка')
    else:
        print(x[0]) # "отрезали" первый элемент
        func(x[1:])

func(my_list)