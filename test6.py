# Урок № 8, задание 1
n=int(input('Введите число N, N больше или равно 1, но меньше или равно 10000: '))
list1=[]
for i in range(n):
    a=int(input())
    list1.append(a)
list1.reverse()
print(list1)

# Урок № 8, задание 2
m=int(input('Введите число, которое больше или равно 1, но меньше или равно 100000: '))
list2=[]
for i in range(m):
    b=int(input())
    list2.append(b)
element=list2.pop(-1)
list2.insert(0, element)  #list2.insert(0,list2.pop(-1))
print(list2)

# Урок № 8, задание 3
k=int(input('Введите максимальную массу, которую может выдержать одна лодка (от 1 до 10е6): '))
l=int(input('Введите количество рыбаков (от 1 до 100): '))
list3=[]
for i in range(l):
    Ai=int(input('Введите вес рыбака (его вес не должен быть больше максимальной подъемности лодки, иначе он не сможет отправиться на противоположный берег): '))
    list3.append(Ai) # Создали список из веса рыбаков
    list3.sort(reverse=True) # отсортировали вес в порядке убывания

for j in range(len(list3)): # перебираем значения веса в списке
    for q in range(j+1, len(list3)):
        if (list3[j]+list3[q]) <= k:
            list3.pop(q)
            break
print('Минимальное количество лодок, необходимое для переправки всех рыбаков на противоположный берег: ', len(list3))
