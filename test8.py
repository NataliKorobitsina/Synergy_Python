# Урок № 10, задание 1
pets={}
name=input('Введите имя питомца: ')
info={}
pets[name]=info
pets[name]['Вид питомца']=input('Введите вид питомца: ')
pets[name]['Возраст питомца:']=int(input('Введите возраст питомца: '))
pets[name]['Имя владельца:']=input('Введите имя владельца: ')

old=pets[name]['Возраст питомца:']
if old%10==1:
    year='год'
elif 2<=old<=4 or 22<=old<=24:
    year='года'
else:
    year='лет' # вряд ли какие-то домашние животные живут дольше 30 лет

key=list(pets[name].keys())
val=list(pets[name].values())

print('Это', val[0], 'по кличке',name, end='. ')
print(key[1], val[1], year, end='. ')
print(key[2], val[2])



# Урок № 10, задание 2
my_dict={i:i**i for i in range(10,-6,-1)}
print(my_dict)
