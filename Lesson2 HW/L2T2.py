
#myvar=646544566650900001
mylist=[]
myresult=[]
i=0
while True:
    myvar = input('Ведите элемент списка или слово "stop", если введение списка закончилось')
    if myvar=="stop":
       break
    mylist.append(myvar)
zi=0
print(f"Исходный ряд:",mylist)
LEN=len(mylist)
#print(f"LEN=",LEN)

#print(mylist[zi+1])
#print(mylist[zi])
#myresult.insert (0,mylist[z+1])
#print(myresult)
#lenth=len(mylist)
#print(lenth)

#if lenth%2 != 0:
#    lenth = lenth-1
a1=0
a2=0
while True:
  #print(mylist[(zi+1)])
 a1=mylist[(zi+1)]
 a2=mylist[zi]
 #print(zi)
 myresult.append(a1)
 myresult.append(a2)
 zi=zi+2
 if zi>=(LEN-1):
     break
if len(myresult)<LEN:
  myresult.append(mylist[(len(mylist)-1)])
print(f"Результат:",myresult)
