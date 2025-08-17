# Урок № 4, задание 1
a=float(input('Введите длину прямоугольника: '))
b=float(input('Введите ширину прямоугольника: '))
s=a*b
p=2*(a+b)
print('Площадь прямоугольника: ', s)
print('Периметр прямоугольника: ', p)

# Урок № 4, задание 2
number=int(input('Введите пятизначное число: '))
ed=number%10
des=number%100//10
sot=number%1000//100
th=number%10000//1000
ten=number%100000//10000
print((des**ed)*sot/(ten-th))

