
class Cell:

    def __init__(self,cells):
        self.cells=int(cells)

    def __repr__(self):
        return str(self.cells)

    def __add__(self, other):
        return Cell(self.cells + other.cells)

    def __sub__(self, other):
        if self.cells==other.cells:
            print("Ошибка! Экземпляры классов содержат одинаковое количество ячеек, вычитание невозможно!")
        else: return Cell(self.cells - other.cells)

    def __mul__(self, other):
        return Cell(self.cells * other.cells)

    def __truediv__(self, other):
        return Cell(self.cells // other.cells)

    def make_order(self,string):
        mylist=[]
        self.string = string
        srttimes = self.cells//string
        for i in range(0,self.cells,1):
            if i//(string) == i/(string):
                if i!=0:
                    mylist.append("\n")
                mylist.append("*")
            else: mylist.append("*")
        a=str(mylist).replace(",","")
        a=a.replace("'","")
        a=a.replace("[", "")
        a=a.replace("]", "")
        return print(a)

a=Cell(input("Введите количество ячеек экземпляра класса а:"))
b=Cell(input("Введите количество ячеек экземпляра класса b:"))
print("Экземпляр класса 'а' содержит ячеек:", a)
print("Экземпляр класса 'b' содержит ячеек:", b)

print("Работа метода make_order со значением 3 с экземпляром а:")
a.make_order(3)

c=a.__add__(b)
print("Количество ячеек после сложения экземпляров класса:", c)
c=a.__sub__(b)
print("Количество ячеек после вычитания экземпляров класса:",c)
c=a.__mul__(b)
print("Количество ячеек после умножения экземпляров класса:",c)
c=a.__truediv__(b)
print("Количество ячеек после деления нацело экземпляров класса:",c)
