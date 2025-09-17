# Урок № 13, задание 1
import random
def pl(a): # функция для красивого вывода)
    for m in a:
        print(*m)
x=int(input('Введите число строк: ')) # Количество элементов в списке
y=int(input('Введите число столбцов: ')) # Количество элементов во вложенном списке

matrix_1=[[random.randint(-200, 200) for i in range(y)] for j in range(x)]
matrix_2=[[random.randint(-200, 200) for k in range(y)] for l in range(x)]
print('Первая матрица:')
pl(matrix_1)
print('Вторая матрица:')
pl(matrix_2)

matrix_3=[]
for i in range(x):
    row = [] # Это строка в матрице, внутренний список
    for j in range(y):
        row.append(matrix_1[i][j]+matrix_2[i][j])
    matrix_3.append(row)
print('Матрица суммы:')
pl(matrix_3)
