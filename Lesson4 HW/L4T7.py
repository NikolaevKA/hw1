from itertools import count

#n=10
n=int(input("Введите число, от которого будет найден факториал: "))
mylist2=[]
def fact(n):
    mylist = []
    factv = 1
    for el in count(0):
        if el > n:
            break
        else:
            mylist.append(el)
            #print(mylist)
    for i in range(0,len(mylist)-1,1):
        factv=factv*mylist[i+1]
        yield factv
a = fact(n)
#print(type(a))
for b in fact(n):
    #print(b)
    mylist2.append(b)
print(max(mylist2))
