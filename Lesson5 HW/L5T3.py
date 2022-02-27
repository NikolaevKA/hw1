from statistics import mean

with open("L5T3.txt", "r", encoding="utf-8") as f:
 content=f.read()
mylist=content.split("\n")
# print("Список сотрудников: ", mylist)
listsn=[]
listin=[]
for i in range(0,len(mylist)-1,1):
  snames=(mylist[i].split(" "))[0]
  incomes=int((mylist[i].split(" "))[1])
  listsn.append(snames)
  listin.append(incomes)
  # print(type(snames))
#print(listsn)
#print(listin)
i=0
lowsnames=[]
for i in range(0,len(listin),1):
 if listin[i]<20000:
  lowsnames.append(listsn[i])
print("Сотрудники с ЗП менее 20 000: ", lowsnames)
print("среднее значение ЗП:", mean(listin))



