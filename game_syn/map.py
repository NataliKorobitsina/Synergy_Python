from utils import randbool
from utils import randcell
from utils import randcell2
from helicopter import Helicopter as Helico

"""карта - двумерный список, элементами которого будут клеточки (дерево, пустое поле, вода).
В каждой клеточке храним число, которое показывает что там находится"""
# 0 - поле
# 1 - дерево
# 2 - река
# 3 - госпиталь
# 4 - апгрейд-шоп
# 5 - огонь

CELL_TYPES = '🟩🌲🌊🏥🏪🔥'
TREE_BONUS = 100 # очки за спасённое едерево
UPGRADE_COST = 5000 # количество очков для модернизации

class Map:

    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells = [[0 for i in range(w)] for j in range(h)] # везде поле ("0"). w клеточек в h строке
        self.generate_forest(3,10)
        self.generate_river(10)
        self.generate_river(10)
        self.generate_upgrade_shop()
    
    def check_bounds(self, x, y): # проверка границ
        if (x < 0) or (y < 0) or (x >= self.h) or (y >= self.w): # x направлена из левой клетки вниз, y - направо
            return False
        return True
    
    def print_map(self, helico):
            print('⬛️' * (self.w + 2))
            for ri in range(self.h): # row на каждом шаге принимает значение из списка cells (значение ряда)
                print('⬛️', end='')
                for ci in range(self.w): # в каждом ряду перебираем клеточку
                    cell = self.cells[ri][ci]
                    if helico.x == ri and helico.y == ci:
                        print('🚁', end='')
                    elif cell >= 0 and cell < len(CELL_TYPES): # не выйдем за границы строки
                        print(CELL_TYPES[cell], end='')
                print('⬛️')
            print('⬛️' * (self.w + 2))

    def generate_river(self, l): # l - длина реки
        rc = randcell(self.w, self.h)  # клеточка - начало реки
        rx, ry = rc[0], rc[1]
        self.cells[rx][ry] = 2
        while l > 0:
            rc2 = randcell2(rx, ry)
            rx2, ry2 = rc2[0], rc2[1] 
            if self.check_bounds(rx2, ry2): # проверяем клетку на принадлежность к границам
                self.cells[rx2][ry2] = 2
                rx, ry = rx2, ry2
                l-=1

    def generate_forest(self, r, mxr): # r - отсечка, mxr - диапазон рандома
        for ri in range(self.h):
            for ci in range(self.w):
                if randbool(r, mxr):
                    self.cells[ri][ci] = 1

    def generate_tree(self): # генерирует клетку, если она не занята - ставит туда дерево. Если занята - ничего
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if self.cells[cx][cy] == 0: # проверяем, что эта клетка с полем
            self.cells[cx][cy] = 0

    def generate_upgrade_shop(self):
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        self.cells[cx][cy] = 4

    def add_fire(self): # добавляем огонь
        c = randcell(self.w, self.h) # рандомная клеточка
        cx, cy = c[0], c[1]
        if self.cells[cx][cy] == 1: # проверяем, что там дерево
            self.cells[cx][cy] = 5

    def update_fires(self): # удаляет огни, которые сгорели и добавляет новые
        for ri in range(self.h): # проходимся по всем огням, которые не потушили
            for ci in range(self.w):
                cell = self.cells[ri][ci]
                if cell == 5:
                    self.cells[ri][ci] = 0 # на их место ставим поле и добавляем до 5 огней
        for i in range(10):
            self.add_fire()

    def process_helicopter(self, helico): # пополняем вертолет водой, когда аходимся над рекой
        c = self.cells[helico.x][helico.y] # координаты вертолета в отдельной переменной
        if c == 2: # если на ячейке река
            helico.tank = helico.mxtank # в резервуаре столько воды, сколько он вмещает
        if c == 5 and helico.tank > 0:
            helico.tank -= 1 # отнимаем одну ячейку воды, когда над огнём
            self.cells[helico.x][helico.y] = 1 # в этой ячейке теперь спасённое дерево
            helico.score += TREE_BONUS
        if c == 4 and helico.score >= UPGRADE_COST: # модернизация, если достаточно очков
            helico.mxtank += 1
            helico.score -= UPGRADE_COST
    







