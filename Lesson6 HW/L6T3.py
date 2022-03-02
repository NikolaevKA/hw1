
class Worker:
    # атрибуты класса
    def __init__(self,name,surname,position,wage,bonus):
     self.name = name
     self.surname = surname
     self.position = position
     self._income = dict(wage=wage,bonus=bonus)

class Position(Worker):
    def get_full_name(self):
        print(self.name,self.surname)

    def get_total_income(self):
        print(sum(self._income.values()))

b=Position("Александр","Шамаев","грузчик",70000, 30000)
b.get_full_name()
b.get_total_income()