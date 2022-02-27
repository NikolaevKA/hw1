#{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
from statistics import mean
import json
mylist=[]
with open("L5T7.txt", "r", encoding="utf-8") as f:
    while True:
        content = f.readline()
        #print(content)
        mylist.append(content)
        if not content:
            break
#print(mylist)

listfirms=[]
listnames=[]
#listforms=[]
listincome=[]
listcost=[]
listprofit=[]

for i in range(0,len(mylist)-1,1):
   listfirms.append(mylist[i].split("\n")[0])
   listnames.append(listfirms[i].split(" ")[0])
   #listforms.append(listfirms[i].split(" ")[1])
   listincome.append(int(listfirms[i].split(" ")[2]))
   listcost.append(int(listfirms[i].split(" ")[3]))
   listprofit.append(listincome[i]-listcost[i])

# print(listfirms)
# print(listnames)
# print(listforms)
# print(listincome)
# print(listcost)
# print(listprofit)

mydict ={}
mydict2 ={}
myresultlist=[]
for i in range(0,len(listnames),1):
     mydict[listnames[i]]=listprofit[i]
mydict2=dict(average_profit=mean(listprofit))
myresultlist.append(mydict)
myresultlist.append(mydict2)
#print(mydict)
#print(mydict2)
#print(myresultlist)
with open("L5T7.json", "w") as j_f:
    json.dump(myresultlist, j_f)