def myfunction(num_1,num_2):
    if num_2==0:
        print("пожалуйста, измените знаменатель на занчение, отличное от 0")
    else: return num_1/num_2
num_1=int(input('Введите числитель: '))
num_2=int(input('Введите знаменатель: '))

print(f'Резульат расчета заданной функции:')
print (myfunction(num_1,num_2))
