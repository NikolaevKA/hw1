mylist=[]
with open("L5T4.txt", "r", encoding="utf-8") as f:
    while True:
        content = f.readline()
        #print(content)
        mylist.append(content)

        if not content:
            break

#print(mylist)
listsn=[]
listin=[]
for i in range(0,len(mylist)-1,1):
  snames=(mylist[i].split(" — "))[0]
  incomes=(mylist[i].split(" — "))[1]
  listsn.append(snames)
  listin.append(incomes)
  # print(type(snames))
#print(listsn)
#print(listin)
ruslist=["Один", "Два", "Три", "Четыре"]

with open("L5T4_res.txt", "w", encoding="utf-8") as f_res:
    for i in range(0,len(listin),1):
     print(ruslist[i]," — ",listin[i],file=f_res)
# i=0
# lowsnames=[]
# for i in range(0,len(listin),1):
#  if listin[i]<20000:
#   lowsnames.append(listsn[i])
# print("Сотрудники с ЗП менее 20 000: ", lowsnames)
# print("среднее значение ЗП:", mean(listin))


