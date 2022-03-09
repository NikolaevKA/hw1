
class OwnError(Exception):
   def __init__(self, txt):
     self.txt = txt

inp_data = 0
mylist=[]
while inp_data!="stop":
 inp_data = input("Введите число, или stop для завершения ввода: ")


 try:
     if inp_data!="stop":
      if inp_data.isdigit() != True:
       raise OwnError("Необходимо ввести число!")
     else: break
 except OwnError as err:
     print(err)
 else:
     mylist.append(int(inp_data))
print(mylist)