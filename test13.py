# Урок № 16, задание 1
class Kassa(object):
    cash=15000 # количество денег в кассе

    def top_up(self, x): # пополнить на X
        self.cash+=x

    def count_1000(self): # выводит сколько целых тысяч осталось в кассе
        return self.cash//1000

    def take_away(self, y): # забрать y из кассы
        self.cash-=y
        if y > self.cash:
            print('Недостаточно денег в кассе!')

tmp=Kassa() # для примера
tmp.top_up(680)
print(tmp.cash)
print(tmp.count_1000())
tmp.take_away(750)
print(tmp.cash)
tmp.take_away(15000)



# Урок № 16, задание 2
class Turtle(object):
    x=0
    y=0
    s=0

    def __init__(self, x, y, s):
        self.x=x
        self.y=y
        self.s=s

    def go_up(self, s):
        self.y+=s

    def go_down(self, s):
        self.y-=s

    def go_left(self, s):
        self.x-=s

    def go_right(self, s):
        self.x+=s

    def evolve(self):
        self.s+=1

    def degrade(self):
        self.s-= 1
        if self.s <=0:
            print('Ошибка!!!')

    def count_moves(self, x2, y2):
        diff_x=abs(abs(x2)-abs(self.x))
        diff_y=abs(abs(y2)-abs(self.y))
        return diff_x+diff_y

turtle1=Turtle(2,-5,4) # для примера
turtle1.go_up(1)
print('y =', turtle1.y)
turtle1.go_down(4)
print('y =', turtle1.y)
turtle1.go_left(-1)
print('x =', turtle1.x)
turtle1.go_right(2)
print('x =', turtle1.x)
turtle1.evolve()
print('s =', turtle1.s)
turtle1.degrade()
print('s =', turtle1.s)
print(turtle1.count_moves(0, 0))
