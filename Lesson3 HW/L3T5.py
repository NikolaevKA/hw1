def my_func (myvar):
    mylist = myvar.split(" ")
    mylist2=[]
    mywords=[]
    for i in range(0,len(mylist),1):
            if mylist[i].isdigit():
               mylist2.append(int(mylist[i]))
            else: mywords.append(mylist[i])
    #print(mylist2)
    #print(mywords)
    return dict(numbers=mylist2, notnumbers=mywords)
summary=0
mynum=[]
mynnum=[]
while True:
  myvar = input('Введите числа через пробел, и/или знак @, если хотите завершить ввод: ')
  if myvar == "@":
      break
  mylist = my_func(myvar)
  #print(mylist)
  mynum=mylist.get("numbers")
  mynnum=mylist.get("notnumbers")
  #print(mynum)
  print('Сумма введенных чисел равна: ')
  summary=summary+sum(mynum)
  print(summary)
  if mynnum.count("@")!=0:
       break

