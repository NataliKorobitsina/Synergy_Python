# Урок № 5, задание 1
num=int(input('Введите целое число: '))

if (num>0) and (num%2==0):
    print('Положительное четное число')
elif (num>0) and (num%2!=0):
    print('Положительное нечетное число')
elif (num<0) and (num%2==0):
    print('Отрицательное четное число')
elif (num<0) and (num%2!=0):
    print('Отрицательное нечетное число')
else:
    print('Это ноль')


# Урок № 5, задание 2
w=input('Введите слово из маленьких латинских букв: ')

if ('a' in w) and ('e' in w) and ('i' in w) and ('o' in w) and ('u' in w):
    a=w.count('a')
    e=w.count('e')
    oi=w.count('i')
    o=w.count('o')
    u=w.count('u')
    gls=a+e+oi+o+u
    print('Гласных букв в слове: ', gls)
    print('Из них', '\'a\'', a, ',', '\'e\'', e, ',', '\'i\'', oi, ',', '\'o\'', o, ',', '\'u\'', u)
    sgl=len(w)-gls
    print('Согласных букв в слове:', sgl)
else:
    print(False)


# Урок № 5, задание 3
inv=1000
print('Минимальная сумма инвестиций: ', inv)
mike=int(input('Введите сумму, которой располагает Майкл: '))
ivan=int(input('Введите сумму, которой располагает Иван: '))

if (mike>=inv) and (ivan>=inv):
    print(2)
elif (mike>=inv) and (ivan<inv):
    print('Mike')
elif (ivan>=inv) and (mike<inv):
    print('Ivan')
elif (mike<inv) and (ivan<inv) and ((mike+ivan)>=inv):
    print(1)
else:
    print(0)

