myvar = int((input('Введите натуральное число ')))
mylist=[10,8,6,4,2]
exist=(mylist.count(myvar))
myvar2=myvar
if exist!=0:
 pos = mylist.index(myvar)
 mylist.insert(pos, myvar)
elif max(mylist)<myvar:
   mylist.insert(0, myvar)
elif min(mylist)>myvar:
       mylist.insert(len(mylist), myvar)
else:
 while True:
       myvar2=myvar2+1
       exist=(mylist.count(myvar2))
       if exist!=0:
        mylist.insert(mylist.index(myvar2)+1, myvar)
        break
#print(mylist.index(myvar2))
print(mylist)
