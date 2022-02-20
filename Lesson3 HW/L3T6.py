def int_func (myvar):
    mylist = myvar.title()
    return mylist

myvar=input("Веедите текстовую строку из нескольких слов из маленьких латинских букв: ")
result=int_func(myvar)
print(result)

