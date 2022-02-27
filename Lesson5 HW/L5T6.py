#{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
mylist=[]
with open("L5T6.txt", "r", encoding="utf-8") as f:
    while True:
        content = f.readline()
        #print(content)
        mylist.append(content)
        if not content:
            break
#print(mylist)

listst=[]
listnames=[]
lekcii=[]
pract=[]
labs=[]
lekcii2=[]
pract2=[]
labs2=[]
for i in range(0,len(mylist)-1,1):
  listst.append(mylist[i].split("\n")[0])
  listnames.append(listst[i].split(" ")[0])
  lekcii.append(listst[i].split(" ")[1])
  pract.append(listst[i].split(" ")[2])
  labs.append(listst[i].split(" ")[3])
#   # print(type(snames))
# print(listst)
# print(listnames)
# print(lekcii)
# print(pract)
# print(labs)
for i in range(0,len(lekcii),1):
 lekcii2.append(lekcii[i].split("(л)")[0])
 if lekcii2[i].isdigit() == True:
     #print(lekcii2[i].isdigit())
     lekcii2[i]=int(lekcii2[i])
 else: lekcii2[i]=0
#print(lekcii2)
for i in range(0,len(pract),1):
 pract2.append(pract[i].split("(пр)")[0])
 if pract2[i].isdigit() == True:
     #print(lekcii2[i].isdigit())
     pract2[i]=int(pract2[i])
 else: pract2[i]=0
#print(pract2)
for i in range(0,len(labs),1):
 labs2.append(labs[i].split("(лаб)")[0])
 if labs2[i].isdigit() == True:
     #print(lekcii2[i].isdigit())
     labs2[i]=int(labs2[i])
 else: labs2[i]=0
#print(labs2)

mydict ={}
for i in range(0,len(listnames),1):
    mydict[listnames[i].replace(":","")]=lekcii2[i]+pract2[i]+labs2[i]
print(mydict)
