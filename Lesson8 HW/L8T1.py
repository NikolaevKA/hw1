
class Date:
    def __init__(self,Date_input):
     self.date=Date_input

    @classmethod
    def str_to_int(cls,Date_input):
        mylist=Date_input.split("-")
        day=int(mylist[0])
        month=int(mylist[1])
        year=int(mylist[2])
        return print(day,month,year)
    @staticmethod
    def validation(Date_input):
        mylist=Date_input.split("-")
        if int(mylist[0]) not in range(1,32,1):
            print("Введенная дата не прошла валидацию даты!")
        elif int(mylist[1]) not in range(1,13,1):
            print("Введенная дата не прошла валидацию месяца!")
        elif int(mylist[2]) not in range(1,3000,1):
            print("Введенная дата не прошла валидацию года!")
        else: print("Введенная дата прошла валидацию!")

a=input("Введите дату в формате день-месяц-год:")
Date.str_to_int(a)
Date.validation(a)
