from itertools import count
from itertools import cycle

start=int(input('Введите стартовое целочисленное значение ряда: '))
stop=int(input('Введите завершающее целочисленное значение ряда: '))
stop2=int(input('Введите число повторов ряда: '))
mylist=[]
for el in count(start):
    if el > stop:
        break
    else:
        mylist.append(el)
print("Результат генерации ряда: ")
print(mylist)
newlist=[]
с = 0
for el in cycle(mylist):
    if с >= stop2*len(mylist):
        break
    newlist.append(el)
    с += 1
print("Результат повтора ряда по заданному количеству повторов: ")
print(newlist)


