from utils import randcell

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
        
    def move(self, dx, dy): # получаем новые координаты вертолета
        nx, ny = dx + self.x, dy + self.y
        if nx >= 0 and ny >= 0 and nx < self.h and ny < self.w:
            self.x, self.y = nx, ny

    def print_stats(self):
        print('💧 ', self.tank, '/', self.mxtank, sep='', end=' | ', )
        print('🏆', self.score)



