class OwnError(Exception):
   def __init__(self, txt):
     self.txt = txt

class Warehause:

    def __init__(self):
        self.warehause = {}

    def load_in(self, other):
          self.warehause[other.ser_num] = other.brand
          print("На склад принят",other.brand,"с серийным номером",other.ser_num)

    def load_out(self, taker, other):
        # print(self.warehause.values())
        # print(other.ser_num)
        if other.ser_num in self.warehause.keys():

            self.warehause.pop(other.ser_num)
            print("Со склада отгружен", other.brand, "с серийным номером", other.ser_num, "получателю", taker)
    def __repr__(self):
        return str(self.warehause)

class Office_equipment:
     def __init__(self):
         pass

class Printer(Office_equipment):
    ser_num = 10000
    def __init__(self, brand, paperformat, color, perfomance, copyes_per_fillment):

        self.brand = brand
        self.color = color
        self.pf = paperformat
        self.pfm = perfomance

        self.copyes_per_fillment = copyes_per_fillment
    ser_num +=1
    def __repr__(self):
      return str(dict(ser_num = self.ser_num,brand = self.brand,color =self.color,paperformat=self.pf,perfomance = self.pfm, copyes_per_fillment=self.copyes_per_fillment))


class Scaner(Office_equipment):
    ser_num = 20000
    def __init__(self, brand, paperformat, perfomance, load_type):
        self.brand = brand
        self.pf = paperformat
        self.pfm = perfomance
        self.lt = load_type
    ser_num += 1

    def __repr__(self):
        return str(dict(ser_num=self.ser_num, brand=self.brand, paperformat=self.pf, perfomance=self.pfm,load_type = self.lt))


class Copyer(Office_equipment):
    ser_num = 30000

    def __init__(self, brand, paperformat, perfomance, load_type, copyes_per_fillment):
        self.brand = brand
        self.pf = paperformat
        self.pfm = perfomance
        self.lt = load_type
        self.copyes_per_fillment = copyes_per_fillment
    ser_num += 1

    def __repr__(self):
        return str(
            dict(ser_num=self.ser_num, brand=self.brand, paperformat=self.pf, perfomance=self.pfm, load_type=self.lt, copyes_per_fillment=self.copyes_per_fillment))

#
# b=Printer("Xerox","A4","mono",120,3000)
# c=Scaner("Toshiba","A4",60,"pack")
# e=Copyer("Samsung","A3",200,"pack",15000)
# print ("Создан принтер с параметрами:",b)
# print ("Создан сканер с параметрами:",c)
# print ("Создан копир с параметрами:",e)
#
# w=Warehause()
# w.load_in(b)
# # print (w)
# w.load_out("Отдел Маркетинга",b)
# # print (w)
# w.load_in(c)
# w.load_out("Приемная директора",c)
# w.load_in(e)
# w.load_out("Бухгалтерия",e)

print("Добро пожаловать в программу складского учета оргтехники! Следуйте инструкциям и Вы быстро научитесь!")
type_it=input("Сначала необходимо выбрать вид оргтехники, которую мы заведем на склад, введите 1, если это принтер, 2 если это сканер и 3 если это копир :")

try:
   if int(type_it) not in range(1,4,1):
     raise OwnError("Необходимо ввести число 1,2 или 3!")
except ValueError:
   print("Вы ввели не число!")
except OwnError as err:
     print(err)
# print(type_it)
if type_it.isdigit() != True:
    exit()
if int(type_it) not in range(1,4,1):
    exit()
if int(type_it) !=3:
    print("Вы выбрали не копир, но в настоящее время учебная программа сделана только под копир, поэтому будем создавать копир)")
type_it=3

brand_it=input("Отлично, теперь введите брэнд компании-производителя, например Xerox:")
paperformat_it=input("Отлично, теперь введите формат бумаги копира, например А4: ")
lt_it=input("Отлично, укажите тип загрузки исходника в сканер, pack если лоток, plan, если сканирующая поверхность: ")
# print(lt_it)
try:
   if lt_it!="plan" and lt_it!="pack":
       raise OwnError("Вы ввели не то!")
except OwnError as err:
    print(err)
if lt_it!="plan" and lt_it!="pack":
    exit()

perfomance_it=input("Отлично, укажите производительность копира страниц в минуту, например 120: ")

try:
   if perfomance_it.isdigit()!=True:
       raise OwnError("Вы ввели не число!")
except OwnError as err:
    print(err)
if perfomance_it.isdigit() != True:
    exit()

cpf_it = input("Отлично, последний параметр, введите количество копий на одну заправку, например 5000: ")

try:
   if cpf_it.isdigit()!=True:
     raise OwnError("Вы ввели не число!")
except OwnError as err:
    print(err)
if cpf_it.isdigit() != True:
    exit()

a=Copyer(brand_it,paperformat_it,perfomance_it,lt_it,cpf_it)
print("В базу добавлен копир копир с параметрами:",a)
go_1=input("Для ускорения, добавим в базу еще принтер и сканер с заданными параметрами, если согласны, введите 1: ")

try:
   if go_1.isdigit()!=True:
     raise OwnError("Вы ввели не число!")
except OwnError as err:
    print(err)
if go_1.isdigit() != True or go_1!= "1":
    exit()

b=Printer("Xerox","A4","mono",120,3000)
c=Scaner("Toshiba","A4",60,"pack")
print ("В базу добавлен принтер с параметрами:",b)
print ("В базу добавлен сканер с параметрами:",c)

go_2=input("Теперь примем на склад все 3 объекта, если согласны, введите 1: ")

try:
   if go_2.isdigit()!=True:
     raise OwnError("Вы ввели не число!")
except OwnError as err:
    print(err)
if go_2.isdigit() != True or go_1!= "1":
    exit()

w=Warehause()
w.load_in(a)
w.load_in(b)
w.load_in(c)
print("Отлично, давайте посмотрим на отчет склада после приемки наших объектов")
print (w)

print("Мы научились создавать объекты в базе и принимать их на склад. Отлично! Настало время научиться их отгружать по заказ-наряду")
go_3=input("У нас 3 заказ-наряда на отгрузку, 1. Копир в бухгалтерию, 2. Принтер в приемную директора, 3. Сканер в отдел маркетинга, введите 1,2 или 3 для выбора заказ-наряда: ")

try:
   if int(go_3) not in range(1,4,1):
     raise OwnError("Необходимо ввести число 1,2 или 3!")
except ValueError:
   print("Вы ввели не число!")
except OwnError as err:
     print(err)
# print(type_it)
if go_3.isdigit() != True:
    exit()
if int(go_3) not in range(1,4,1):
    exit()
if go_3=="1":
 w.load_out("Бухгалтерия",a)
if go_3=="2":
 w.load_out("Приемная директора",b)
if go_3=="3":
 w.load_out("Отдел маркетинга",c)

print("Отлично, давайте посмотрим на отчет склада после отгрузки")
print (w)
print("Поздравляем, ваше обучение прошло успешно!")


