myvar=int(input('Ведите целоe положительное число (не больше 18 цифр): '))
#myvar=646544566650900001
mylist=[]
i=0
while i<100:
    i=i+1
    if myvar==0:
        break
    myvar2 = int(myvar)%10
    myvar =int((myvar-myvar2)/10)
    #print(myvar)
    mylist.append(myvar2)
#print(mylist)
print(max(mylist))










