
class Road:
    # атрибуты класса
    def __init__(self,length,width,heght=5,massa1=25):
     self._length = length
     self._width = width
     self.heght = heght
     self.massa1 = massa1

    # методы класса
    def mass(self):
        print("Для покртытия поверхности длинной",self._length,"метров, шириной",self._width,"метров и толщиной", self.heght,"см, понадобится", self._length*self._width*self.massa1*self.heght/1000, "тонн асфальта")

b=Road(200,25)
b.mass()
