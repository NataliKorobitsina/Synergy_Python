from utils import randcell
import os

class Helicopter:
    def __init__(self, w, h):
        rc = randcell(w, h) # генерация начального положения вертолёта
        rx, ry = rc[0], rc[1]
        self.x = rx
        self.y = ry
        self.h = h
        self.w = w
        self.tank = 0 # изначально 0, так как еще не заполнили водой
        self.mxtank = 1 # вместимость вертолета начальная
        self.score = 0 # очки за каждое спасённое дерево
        self.lives = 20 # жизни)
        
    def move(self, dx, dy): # получаем новые координаты вертолета
        nx, ny = dx + self.x, dy + self.y
        if (nx >= 0) and (ny >= 0) and (nx < self.h) and (ny < self.w):
            self.x, self.y = nx, ny

    def print_stats(self):
        print('💧 ', self.tank, '/', self.mxtank, sep='', end=' | ')
        print('🏆', self.score, end=' | ')
        print('💛', self.lives)
        
    def game_over(self):
        # global helico
        os.system('cls')
        print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
        print('')
        print('GAME OVER, YOUR SCORE IS', self.score)
        print('')
        print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
        exit(0)

    def export_data(self): # сохранили все данные, которые касаются вертолёта
        return {'score': self.score, 
                'lives': self.lives, 
                'x': self.y, 'y': self.y, 
                'tank': self.tank, 'mxtank': self.mxtank}
    
    def import_data(self, data): # функция импортер
        self.x = data['x'] or 0 # в случае если ошибка в json - мы выводим 0
        self.y = data['y'] or 0
        self.tank = data['tank'] or 0
        self.mxtank = data['mxtank'] or 1
        self.lives = data['lives'] or 3
        self.score = data['score'] or 0

