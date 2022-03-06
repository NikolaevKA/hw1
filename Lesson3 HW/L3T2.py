def myfunction(name, surname, yob, city, email, cellphone):
    return print("Имя: " + name + " Фамилия: " + surname + " Год_рождения: " + yob + " Город_проживания:" + city + " email: " + email + " Мобильный: " + cellphone)

name=input('Введите имя: ')
surname=input('Введите фамилию: ')
yob=input('Введите год рождения: ')
city=input('Введите город проживания: ')
email=input('Введите адрес электронной почты: ')
cellphone=input('Введите номер мобильного телефона: ')

print(f'Досье на вас: ')
myfunction(name, surname, yob, city, email, cellphone)
