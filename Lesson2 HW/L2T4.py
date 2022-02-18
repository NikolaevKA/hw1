myvar = (input('Напишите предложение из нескольких слов: '))
#myvar = "Я твой кепка тапталтапталата"
mylist=myvar.split(" ")
print(mylist)
i=0
while i<=len(mylist)-1:
        print(i+1,'. ', mylist[i][0:10])
        i=i+1