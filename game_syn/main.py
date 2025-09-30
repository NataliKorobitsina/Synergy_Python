from map import Map
import time
import os
from helicopter import Helicopter
from pynput import keyboard

TICK_SLEEP = 0.05 # установили константу 0.05
TREE_UPDATE = 50 # Устанавливаем новое дерево каждые 50 тиков
FIRE_UPDATE = 100 # сколько горит пожар до обновления
MAP_W, MAP_H = 20, 10 # размер поля

tmp = Map(MAP_W, MAP_H)

helico = Helicopter(MAP_W, MAP_H)

MOVES = {'w':(-1,0), 'd':(0, 1), 's':(1, 0), 'a':(0, -1)} # по ключу буквы возвращает насколько мы должны переместиться

def pcocess_key(key): # клавиши
    global helico
    c = key.char.lower()
    if c in MOVES.keys():
        dx, dy = MOVES[c][0], MOVES[c][1]
        helico.move(dx, dy)
listener = keyboard.Listener(on_press = None, on_release = pcocess_key)
listener.start()

tick = 1 # переменная показывает какой сейчас кадр отрисовывается

while True: # до тех пор, пока не завершится программа или не остановим цикл принудительно
    os.system('cls') # очищаем консоль перед каждым выводом
    print('TICK', tick)
    tmp.process_helicopter(helico) # функции вертолёта
    helico.print_stats() # меню
    tmp.print_map(helico) # карта
    tick += 1
    time.sleep(TICK_SLEEP) # сколько ждать после отрисовки кадра
    if tick % TREE_UPDATE == 0: # Устанавливаем новое дерево каждые TREE_UPDATE тиков
        tmp.generate_tree()
    if tick % FIRE_UPDATE == 0: # Генерируем пожар каждые FIRE_UPDATE тиков
        tmp.update_fires()
