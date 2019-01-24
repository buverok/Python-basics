__author__ = 'Фещук Олег Анатольевич'

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

from math import sqrt

class Triangle:
    def __init__(self,A, B, C):
        self.A = A
        self.B = B
        self.C = C

        def side_len(dot1,dot2):
            return sqrt((dot1[0]-dot2[0])**2+(dot1[1]-dot2[1])**2)

        self.AB= side_len(self.A,self.B)
        self.BC= side_len(self.B,self.C)
        self.CA= side_len(self.C,self.A)

    def perimeter(self):
        return self.AB+self.BC+self.CA

    def vysota(self):
        p=triangle1.perimeter()/2
        return 2/self.AB*sqrt(p*(p-self.AB)*(p-self.BC)*(p-self.CA))

    def area(self):
        return self.AB*triangle1.vysota()/2

triangle1 = Triangle((15,12),(33,22),(12,22))

print(triangle1.perimeter())
print(triangle1.vysota())
print(triangle1.area())


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class TrapeciaES:
    def __init__(self,A, B, C, D):
        self.A = A
        self.B = B
        self.C = C
        self.D = D

        def side_len(dot1,dot2):
            return sqrt((dot1[0]-dot2[0])**2+(dot1[1]-dot2[1])**2)

        self.AB = side_len(self.A,self.B)
        self.BC = side_len(self.B,self.C)
        self.CD = side_len(self.C,self.D)
        self.DA = side_len(self.D, self.A)
        self.AC = side_len(self.A, self.C)
        self.BD = side_len(self.B, self.D)

    def perimeter(self):
        return self.AB+self.BC+self.CD+self.DA

    def area(self):
        if self.AB==self.CD:
            return (self.BC+self.DA)/2*sqrt(self.AB**2-(self.DA-self.BC)**2/4)
        elif self.BC==self.DA:
            return (self.CD+self.AB)/2*sqrt(self.BC**2-(self.AB-self.CD)**2/4)
        else: print('Не равнобедренная фигура')

    def isTrapeciaES(self):
        if self.AB==self.CD or self.BC==self.DA:
            if (abs(self.B[0]-self.A[0])) == abs((self.C[0]-self.D[0])):
                if (abs(self.B[1]-self.A[1])) == (abs(self.C[1]-self.D[1])):
                    return True
                else: return False
            else:return False
        else: return False

trap1 = TrapeciaES((-7, 0), (-5, 8), (5, 8), (7, 0))

if trap1.isTrapeciaES() == True :
    print("Равнобедренная трапеция")
else: print("Не равнобедренная и может не трапеция")
print('периметр', trap1.perimeter())
print('Длины сторон',trap1.AB, trap1.BC, trap1.CD, trap1.DA)
print('Площадь ',trap1.area())