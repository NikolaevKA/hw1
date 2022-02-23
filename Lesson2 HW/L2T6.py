mylist=[]
myresult=[]
i=1
#item="компьютер"
#price=10
#ammount=20
#mether="шт"
while True:
    #item="компьютер"+str(i)
    #price=10+10*i
    #ammount=20+20*i
    #mether="шт"
    item = input('Введите название товара ')
    price = int(input('Введите стоимость товара '))
    ammount = int(input('Введите количество товара '))
    mether = input('Введите ед. измерения товара ')
    ask = int(input('Введите 0 если хотите остановить ввод, или 1, если хотите продолжить ввод товара '))
    mydict = dict(название=item,цена=price,количество=ammount, ед=mether)
    mylist.append(i)
    mylist.append(mydict)
    #print(mylist)
    mytuple=tuple(mylist)
    #print(mytuple)
    myresult.append(mytuple)
    i = i + 1
    mylist.clear()
    if ask == 0:
        break
#  break
 #myset=set(myset)
print(f'Cтруктура данных:')
print(myresult)
myresultdict=dict(myresult)
#print(myresultdict)
zi=1
itemslist = []
pricelist = []
ammountlist = []
metherlist = []
for zi in range(1,i,1):
 mydict2=dict(myresultdict.get(zi))
 #print(mydict2)
 itemslist.append(mydict2.get("название"))
 pricelist.append(mydict2.get("цена"))
 ammountlist.append(mydict2.get("количество"))
 metherlist.append(mydict2.get("ед"))
 zi=zi+1
#print(itemslist)
#print(pricelist)
#print(ammountlist)
metherlist=list(set(metherlist))
analitdict=dict(название=itemslist,цена=pricelist,количество=ammountlist, ед=metherlist)
print(f'Результат анализа:')
print(analitdict)
#zi=0
#myresdict={}
#for zi in range(0,len(myresult)):
#mylist2=myresult[0+zi]
#print(mylist2)
# mylist2=mylist2[1+zi]
# print(mylist2)
# mydict2=dict(mylist2)
# print(mydict2)

# mylist2.clear()
# zi=zi+1
