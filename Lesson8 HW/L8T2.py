
class OwnError(Exception):
   def __init__(self, txt):
     self.txt = txt

inp_data = input("Введите знаминатель х дроби 100/х: ")

try:
     if int(inp_data) == 0:
       raise OwnError("На 0 делить нельзя!")
except ValueError:
     print("Вы ввели не число")
except OwnError as err:
     print(err)
else:
     print("Все хорошо. Результат:",round(100/int(inp_data),2))
