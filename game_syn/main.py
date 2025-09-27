

from map import Map
import time
import os

TICK_SLEEP = 0.05 # установили константу
TREE_UPDATE = 50 # Устанавливаем новое дерево каждые 50 тиков
FIRE_UPDATE = 100 # сколько горит пожар до обновления
MAP_W, MAP_H = 20, 10

tmp = Map(MAP_W, MAP_H)
tmp.generate_forest(3,10)
tmp.generate_river(10)
tmp.generate_river(10)
tmp.add_fire()
tmp.add_fire()
tmp.add_fire()
tmp.add_fire()
tmp.add_fire()
tmp.print_map()

tick = 1 # переменная показывает какой сейчас кадр отрисовывается
while True: # до тех пор, пока не завершится программа или не остановим цикл принудительно
    os.system('cls') # очищаем консоль перед каждым выводом
    print('TICK', tick)
    tmp.print_map()
    tick += 1
    time.sleep(TICK_SLEEP) # сколько ждать после отрисовки кадра
    if tick % TREE_UPDATE == 0: # Устанавливаем новое дерево каждые TREE_UPDATE тиков
        tmp.generate_tree()
    if tick % FIRE_UPDATE == 0:
        tmp.update_fires()
