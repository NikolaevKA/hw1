def my_func (base,degree):
    myvar=base**degree
    #myvar=base
    #for i in range(1,abs(degree),1):
     #  myvar=myvar*base
    #if degree<0:
     #  myvar = 1/myvar
    return myvar


base = int(input('Введите значение основания: '))
degree = int(input('Введите значение степени: '))
print(my_func(base, degree))
