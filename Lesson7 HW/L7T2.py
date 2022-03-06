from abc import ABC
class Clothes(ABC):
    def coat_fabric_count(self):
        pass

    def suit_fabric_count(self):
        pass

class Coat(Clothes):
    # атрибуты класса
    def __init__(self,name,sizelist,sizecount):
        self.name=name
        self.size=sizelist
        self.count=sizecount

    @property
    def coat_fabric_count(self):
        reslist=[]
        for el in self.size:
            i=el/6.5 +0.5
            for z in self.count:
                res=i*z
                reslist.append(res)
            return round(sum(reslist),2)

class Suit(Clothes):
    # атрибуты класса
    def __init__(self,name,heghtlist,sizecount):
        self.name = name
        self.heght = heghtlist
        self.count = sizecount

    @property
    def suit_fabric_count(self):
        reslist = []
        for el in self.heght:
            i = el*2/100 + 0.3
            for z in self.count:
                res = i * z
                reslist.append(res)
            return round(sum(reslist), 2)

sizeslist=[42,44,46,48,50,52,54,56]
heghtlist=[155,160,165,170,175,180,185]
sizescount=[200,300,400,500,400,300,200,100]

a=Coat("WoolCoat",sizeslist,sizescount)
print('Для пальто размеров', sizeslist, "с соотв. количеством изделий для каждого размера", sizescount, "количество необходимой ткани в погонных метрах:", a.coat_fabric_count)
b=Suit("WoolSuit",heghtlist,sizescount)
print('Для костюмов с ростовкой', heghtlist, "с соотв. количеством изделий для каждого роста", sizescount, "количество необходимой ткани в погонных метрах:", b.suit_fabric_count)

