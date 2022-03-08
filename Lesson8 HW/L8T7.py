class ComplexNumOperation:
    # атрибуты класса
    def __init__(self,a,b):
        self.a=int(a)
        self.b=int(b)


    def __str__(self):
        mylist=[]
        mylist.append(str(self.a))
        mylist.append("+")
        mylist.append(str(self.b))
        mylist.append("i")
        res=str(mylist).replace("'","")
        res=res.replace(",","")
        res = res.replace(" ","")
        res = res.replace("[", "(")
        res = res.replace("]", ")")
        return res

    def __add__(self, other):
        res_a=int(self.a)+int(other.a)
        res_b=int(self.b) + int(other.b)
        return ComplexNumOperation(res_a,res_b)
    def __mul__(self, other):
        res_a=int(self.a)*int(other.a)-(int(self.b)*int(other.b))
        res_b=int(self.b)*int(self.a)+(int(self.a)*int(other.b))
        return ComplexNumOperation(res_a,res_b)

print("Добро пожаловать в калькулятор комлексных чисел автораства Никоаева К.А.!")
aa = input("Давайте создадим первое комплексное число. Введите a для выражения (а+bi):")
bb = input("Давайте создадим первое комплексное число. Введите b для выражения (а+bi):")
a=ComplexNumOperation(aa,bb)
print("Наше первое комплексное число:",a)
aa2 = input("Давайте создадим второе комплексное число. Введите a для выражения (а+bi):")
bb2 = input("Давайте создадим второе комплексное число. Введите b для выражения (а+bi):")
b=ComplexNumOperation(aa2,bb2)
print("Наше второе комплексное число:",b)

d=a.__add__(b)
c=a.__mul__(b)
print("Результат сложения комплексных чисел:", d)
print("Результат умножения комплексных чисел:",c)
