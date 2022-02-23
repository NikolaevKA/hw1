def my_func(num_1,num_2,num_3):
    mylist=[num_1,num_2,num_3]
    maximus=max(mylist)
    mylist.remove(maximus)
    maximus2=max(mylist)
    return print(maximus+maximus2)

num_1=int(input('Введите значение 1 для функции: '))
num_2=int(input('Введите значение 2 для функции: '))
num_3=int(input('Введите значение 3 для функции: '))


print(f'Сумма двух наибольших параметров функции равна: ')
my_func(num_1,num_2,num_3)
