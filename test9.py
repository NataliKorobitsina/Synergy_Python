# Урок № 11, задание 1
"""def fact(num):
    f=1
    for i in range (1,num+1):
        f*=i
    return f
res=fact(int(input('Введите целое число: ')))

sp=[]
for j in range(res,0,-1):
    a = fact(j)
    sp.append(a)
print(sp)"""


# Урок № 11, задание 2
import collections
pets = {
    1: {'Фаня':
            {'Вид питомца': 'кот', 'Возраст питомца': 13, 'Имя владельца': 'Наталия'}
        },
    2: {'Деля':
            {'Вид питомца': 'собака', 'Возраст питомца': 8, 'Имя владельца': 'Иван'}
        },
    3: {'Ириска':
            {'Вид питомца': 'кошка', 'Возраст питомца': 6, 'Имя владельца': 'Наталия'}
        },
    4: {'Белка':
            {'Вид питомца': 'кошка', 'Возраст питомца': 6, 'Имя владельца': 'Наталия'}
        }
}
ident=0
name=''
animal=''
age=0
owner=''

def create(): # добавляем запись в базу
    global ident, name, animal, age, owner
    last=collections.deque(pets, maxlen=1)[0]
    ident=last+1
    name=input('Введите имя питомца: ')
    animal=input('Введите вид питомца: ')
    age=int(input('Введите возраст питомца: '))
    owner=input('Введите имя владельца: ')
    pets[ident]={name:{'Вид питомца':animal, 'Возраст питомца':age, 'Имя владельца':owner}}
    print('Информация добавлена. ID вашего питомца',ident)
    return pets # не уверена

def get_pet(pet_id): # возвращает информацию о питомце в виде словаря
    return pets[pet_id] if pet_id in pets.keys() else 'Питомец с таким ID не найден'

def pets_list(): # возвращает список всех питомцев в базе
    for i in pets.keys():
        print(pets[i])

def get_suffix(pet_age): # для отображения суффикса "года"
    if pet_age % 10 == 1:
        suffix = 'год'
    elif 2 <= pet_age <= 4 or 22 <= pet_age <= 24:
        suffix = 'года'
    else:
        suffix = 'лет'
    return suffix

def read(): # отображает информацию о запрашиваемом питомце
    choice=input('Введите формат отображения: словарь, весь список, информация, - ')
    if choice=='словарь':
        pet_id=int(input('Введите ID питомца: '))
        print(get_pet(pet_id))
    elif choice=='весь список':
        print(pets_list())
    elif choice=='информация':
        info=int(input('Введите ID питомца: '))
        if info in pets.keys():
            f=pets[info] # словарь с выбранным питомцем
            pet_name=list(f.keys()) # имя выбранного питомца
            key=list(f[pet_name[0]].keys())
            val=list(f[pet_name[0]].values())
            year=get_suffix(val[1])
            print('Это', val[0], 'по кличке', pet_name[0], end='. ')
            print(key[1], val[1], year, end='. ')
            print(key[2], val[2])
        else:
            print('Питомец с таким ID не найден')
    else:
        print('Введен неверный формат отображения. Повторите ввод.')

def update(): # обновляет информацию об указанном питомце
    update_id=int(input('Введите ID питомца, информацию о котором хотите обновить: '))
    update_name=input('Введите имя питомца, информацию о котором хотите обновить: ')
    a=int(input('Что хотите обновить? (1 - Вид питомца, 2 - Возраст питомца, 3 - Имя владельца): '))
    if a==1:
        pets[update_id][update_name]['Вид питомца']=input('Введите вид питомца: ')
    elif a==2:
        pets[update_id][update_name]['Возраст питомца'] = int(input('Введите возраст питомца: '))
    elif a==3:
        pets[update_id][update_name]['Имя владельца'] = input('Введите имя владельца: ')
    else:
        print('ведена неверная команда)')
    print('Изменения внесены')
    return pets # не уверена

def delete(): # удаляет запись о существующем питомце
    delete_id = int(input('Введите ID питомца, информацию о котором хотите удалить: '))
    del pets[delete_id]
    print('Информация удалена.')
    return pets # не уверена

command=''
while command!='stop':
    command = input('Введите команду create, read, update или delete: ')
    if command=='create':
        create()
    elif command=='read':
        read()
    elif command=='update':
        update()
    elif command=='delete':
        delete()
    elif command=='stop':
        print('Спасибо за использование нашей базы данных, до свидания!')
    else:
        print('Введена неверная команда. Повторите ввод :)')
