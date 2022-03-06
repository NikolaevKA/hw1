
class Car:
    # атрибуты класса
    def __init__(self,speed,color,name,is_police=False):
     self.speed = int(speed)
     self.color = color
     self.name = name
     self.is_police = is_police

    def go(self):
        print("Автомобиль",self.name,"начал движение!")
    def stop(self):
        print("Автомобиль",self.name,'остановился!')
    def turn(self,direction):
        print("Автомобиль", self.name,'повренул', direction)
    def show_speed(self):
        print("Скорость автомобиля",self.speed,"км/ч" )
        if self.classtype==TownCar and self.speed>60:
            print("Зафиксировано превышение скорости!")
        if self.classtype==WorkCar and self.speed>40:
            print("Зафиксировано превышение скорости!")


class TownCar(Car):
    def __init__(self,speed,color,name,is_police):
        super().__init__(speed,color,name,is_police)
        self.classtype = TownCar

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name,is_police)
        self.classtype = SportCar
class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name,is_police)
        self.classtype = WorkCar
class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name,is_police)
        self.classtype = PoliceCar


a=WorkCar("41","GREEN","Mitsubishi",False)
print(a)
print("Цвет авто:",a.color,"Признак 'полиция':",a.is_police)
a.go()
a.show_speed()
a.turn("направо")
a.stop()

b=TownCar("61","BLUE","Lincoln",False)
print(b)
print("Цвет авто:",b.color,"Признак 'полиция':",b.is_police)
b.go()
b.show_speed()
b.turn("налево")
b.stop()

c=SportCar("200","RED","Nissan GT-R",False)
print(c)
print("Цвет авто:",c.color,"Признак 'полиция':",c.is_police)
c.go()
c.show_speed()
c.turn("налево")
c.stop()

d=PoliceCar("150","BLACK","VAZ_2106",True)
print(d)
print("Цвет авто:",d.color,"Признак 'полиция':",d.is_police)
d.go()
d.show_speed()
d.turn("налево")
d.stop()