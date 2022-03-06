
class Stationery:
    # атрибуты класса
    def __init__(self,title):
     self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pan(Stationery):
    def __init__(self,title):
        super().__init__(title)

    def draw(self):
        print("Метод класса",self.title)

class Pancil(Stationery):
    def __init__(self,title):
        super().__init__(title)
    def draw(self):
        print("Метод класса",self.title)
class Handle(Stationery):
    def __init__(self,title):
        super().__init__(title)
    def draw(self):
        print("Метод класса", self.title)

a=Stationery("Дырокол")
print(a)
a.draw()

b=Pan("Ручка")
print(b)
b.draw()

с=Pancil("Карандаш")
print(с)
с.draw()

d=Handle("Маркер")
print(d)
d.draw()
