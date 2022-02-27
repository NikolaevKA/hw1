from random import randint
mylist=[]
mylist2=[]
with open("L5T5.txt", "w") as f:
    for i in range(0, 25, 1):
        f.write(str(randint(1, 100)))
        f.write(' ')
    f.write(str(0))

with open("L5T5.txt", "r") as f:
    for line in f:
        mylist.append(line)
for i in range(0,len(mylist),1):
    mylist2=mylist[i].split(' ')
for i in range(0,len(mylist2),1):
    mylist2[i]=int(mylist2[i])
#print(mylist)
print(sum(mylist2))
# print(mylist)
# print(mylist2)
