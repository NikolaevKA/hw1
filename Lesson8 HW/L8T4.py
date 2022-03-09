class Warehause:

    def __init__(self,address, free_capacity):
        self.address = address
        self.free_capacity = free_capacity

class Office_equipment:
    count=0
    def __init__(self,id,brand,paperformat, color, perfomance):
        self.id = id
        self.brand = brand
        self.color = color
        self.pf = paperformat
        self.pfm = perfomance
    count +=1

class Printer(Office_equipment):
    count = 0
    def __init__(self, copyes_per_fillment):
        self.copyes_per_fillment = cpf
    count +=1
class Scaner(Office_equipment):
    count = 0
    def __init__(self, load_type):
        self.load_type = load_type
    count += 1

class Copyer(Office_equipment):
    count = 0
    def __init__(self, copyes_per_fillment,load_type):
        self.copyes_per_fillment = cpf
        self.load_type = load_type
    count += 1
