
matrix_1=[[31,32],[37,43],[51,86]]
matrix_2=[[3,5,32],[2,4,6],[-1,64,-8]]
matrix_3=[[3,5,8,3],[8,3,7,1]]


class Matrix:
    # атрибуты класса
    def __init__(self,matrix):
        self.strings_num=len(matrix)
        self.colums_num=len(matrix[0])
        self.matrix=matrix

    # методы класса
    # def running(self):
    #     print("Строк в матрице",self.srings_num)
    #     print("Столбов в матрице",self.colums_num)
    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.matrix]))

    #def m_print(self, i, j):
           # print(self._matrix[i][j])
        #for i in range(0,self.strings_num,1):
         #print(str(self.matrix[i]))
    def __add__(self, other):
        m1list=[]
        m2list=[]
        reslist=[]
        reslist2=[]
        #if self.strings_num * self.colums_num > other.strings_num * other.colums_num:
        for i in range(0,self.strings_num,1):
                    for z in range(0,self.colums_num,1):
                        m1list.append((self.matrix[i])[z])
        for i in range(0,other.strings_num,1):
                    for z in range(0,other.colums_num,1):
                        m2list.append((other.matrix[i])[z])
        #print(m1list)
        #print(m2list)
        if len(m1list)>=len(m2list):
            for i in range(0,len(m2list),1):
              reslist.append(m1list[i]+m2list[i])
            for i in range(0,len(m1list)-len(m2list),1):
              reslist.append(m1list[len(m2list)::][i])
        else:
            for i in range(0,len(m1list),1):
              reslist.append(m1list[i]+m2list[i])
            for i in range(0,len(m2list)-len(m1list),1):
              reslist.append(m2list[len(m1list)::][i])
        #print(reslist)
        if len(m1list)>=len(m2list):
            for i in range(0,self.strings_num,1):
             reslist2.append(reslist[0:self.colums_num:1])
             reslist=reslist[self.colums_num::]
        else:
            for i in range(0,other.strings_num,1):
             reslist2.append(reslist[0:other.colums_num:1])
             reslist=reslist[other.colums_num::]
        return Matrix(reslist2)


a=Matrix(matrix_1)
b=Matrix(matrix_2)
c=Matrix(matrix_3)
d=a.__add__(b)
e=d.__add__(c)

print("Matrix_1------------")
print(a)
print("Matrix_2-------------")
print(b)
print("Matrix_3-------------")
print(c)
print("Matrix_1+Matrix_2----")
print(d)
print("Matrix_1+Matrix_2+Matrix_3")
print(e)

