mystartlist=[300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
mynewlist=[]

for i in range(0,len(mystartlist)-1,1):
    if mystartlist[i+1]>mystartlist[i]:
     mynewlist.append(mystartlist[i+1])

print(mynewlist)
