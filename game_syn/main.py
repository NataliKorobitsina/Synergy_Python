from map import Map
import time
import os
from helicopter import Helicopter
from pynput import keyboard
from clouds import Clouds
import json # позволяет превращать словари в json и наоборот

TICK_SLEEP = 0.05 # установили константу 0.05
TREE_UPDATE = 50 # Устанавливаем новое дерево каждые 50 тиков
CLOUDS_UPDATE = 75 # облако каждые 100 тиков
FIRE_UPDATE = 100 # сколько горит пожар до обновления
MAP_W, MAP_H = 20, 10 # размер поля

tmp = Map(MAP_W, MAP_H)
clouds = Clouds(MAP_W, MAP_H)
helico = Helicopter(MAP_W, MAP_H)
tick = 1 # переменная показывает какой сейчас кадр отрисовывается

MOVES = {'w':(-1,0), 'd':(0, 1), 's':(1, 0), 'a':(0, -1)} # по ключу буквы возвращает насколько мы должны переместиться
def pcocess_key(key): 
    global helico, tick, clouds, tmp
    c = key.char.lower()
    # обработка движений вертолёта
    if c in MOVES.keys():
        dx, dy = MOVES[c][0], MOVES[c][1]
        helico.move(dx, dy)
    # сохранение игры
    elif c == 'f':
        data = {'helicopter': helico.export_data(), 
                'clouds': clouds.export_data(), 
                'tmp': tmp.export_data(),
                'tick': tick} # словарь, который хранит всю инфу
        with open ('level.json', 'w') as lvl: # открываем файл на запись
            json.dump(data, lvl) # на основе словаря записывает в json
    # загрузка игры
    elif c == 'g':
        with open('level.json', 'r') as lvl:
            data = json.load(lvl)
            tick = data['tick'] or 1
            helico.import_data(data['helicopter'])
            tmp.import_data(data['tmp'])
            clouds.import_data(data['clouds'])

listener = keyboard.Listener(on_press = None, on_release = pcocess_key)
listener.start()


while True: # до тех пор, пока не завершится программа или не остановим цикл принудительно
    os.system('cls') # очищаем консоль перед каждым выводом
    print('TICK', tick)
    tmp.process_helicopter(helico, clouds) # функции вертолёта
    helico.print_stats() # меню
    tmp.print_map(helico, clouds) # карта
    tick += 1
    time.sleep(TICK_SLEEP) # сколько ждать после отрисовки кадра
    if tick % TREE_UPDATE == 0: # Устанавливаем новое дерево каждые TREE_UPDATE тиков
        tmp.generate_tree()
    if tick % FIRE_UPDATE == 0: # Генерируем пожар каждые FIRE_UPDATE тиков
        tmp.update_fires()
    if tick % CLOUDS_UPDATE ==0:
        clouds.update_clouds()
