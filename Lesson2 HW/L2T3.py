myvar = (input('Ведите номер месяца в году: '))
mydict = dict(key_1='январь',key_2="февраль",key_3="март", key_4="апрель", key_5="май", key_6="июнь", key_7="июль", key_8="август", key_9="сентябрь", key_10="октябрь", key_11="ноябрь", key_12="декабрь")
mylist = ['январь','февраль','март','апрель','май','июнь','июль','август','сентябрь','октябрь','ноябрь','декабрь']
#print("key_" + myvar)

d=mydict.get("key_" + myvar)
myvar = int(myvar)
d2=mylist[myvar-1]

print(f"по версии словаря это: ",d)
print(f"по версии списка это: ",d2)

if myvar in range(1,3,1) or myvar==12:
        print('Зима')

if myvar in range(3,6,1):
        print('Весна')

if myvar in range(6,9,1):
        print('Лето')

if myvar in range(9,12,1):
        print('Осень')

#print(mydict)
#print(mylist)

