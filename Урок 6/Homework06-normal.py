__author__ = 'Фещук Олег Анатольевич'

# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

class Person:
    def __init__(self, name):
        self.name=name

    def get_name(self):
        return self.name


class Student(Person):
    def __init__(self, name, parent1, parent2, classroom):
        Person.__init__(self, name)
        self.parent1=parent1
        self.parent2=parent2
        self.classroom=classroom

    def get_classroom(self):
        return self.classroom

    def get_parents(self):
        return self.parent1, self.parent2

class Teacher(Person):
    def __init__(self, name, subject, classes):
        Person.__init__(self, name)
        self.subject = subject
        self.classes=classes
        self.classroom =[]

    def get_subject(self):
        return self.subject

    def add_classroom(self, classroom):
        self.classroom.append(classroom)

    def get_classrooms(self):
        return self.classes



class School:
    def __init__(self, name):
        self.name=name
        self.classrooms=[]
        self.students=[]
        self.teachers=[]

    def get_classroom(self, classroom):
        self.classrooms.append(classroom)

    def get_classrooms_list(self):
        return self.classrooms

    def get_students_list(self):
        r = 0
        sl = []
        for s in students:
            r += 1
            name=Student.get_name(s)
            print(f'{r}. Ученик {name}')
            sl.append(s)
        return sl

    def get_list_of_classrooms(self):
        for student in students:
            a = Student.get_classroom(student)
            if a not in School.get_classrooms_list(school1950):
                School.get_classroom(school1950, a)
        r = 0
        for i in School.get_classrooms_list(school1950):
            r += 1
            print(f'{r}. Класс {i}')
        return School.get_classrooms_list(school1950)


    def get_students_list_of_class(self):
        School.get_list_of_classrooms(school1950)
        b = int(input('Выберите класс')) - 1
        c = list(School.get_list_of_classrooms(school1950))
        st_l = []
        for student in students:
            a = Student.get_classroom(student)
            if a == c[b]:
                st_l.append(Student.get_name(student))
        x = 0
        for i in st_l:
            x += 1
            print(f'{x}. {i}')

        return st_l

    def get_student_subjects(self):
        School.get_students_list(school1950)
        b = int(input('Выберите ученика')) - 1
        c = list(School.get_students_list(school1950))
        d = Student.get_classroom(c[b])

        subj_l = []
        for i in teachers:
            if d in Teacher.get_classrooms(i):
                subj_l.append(Teacher.get_subject(i))

        print(subj_l)

    def get_student_parents(self):
        School.get_students_list(school1950)
        b = int(input('Выберите ученика')) - 1
        c = list(School.get_students_list(school1950))
        return Student.get_parents(c[b])

    def get_teachers_of_class(self):
        School.get_list_of_classrooms(school1950)
        b = int(input('Выберите класс')) - 1
        c = list(School.get_list_of_classrooms(school1950))
        t_list=[]
        for t in teachers:
            if c[b] in Teacher.get_classrooms(t):
                t_list.append(Teacher.get_name(t))

        return t_list


def menu():
    a = ''
    while a != '0':
        print('1. Получить полный список всех классов школы')
        print('2. Получить список всех учеников в указанном классе')
        print('3. Получить список всех предметов указанного ученика')
        print('4. Узнать ФИО родителей указанного ученика')
        print('5. Получить список всех Учителей, преподающих в указанном классе')
        print('0. Выход')
        a=input('Введите номер команды')
        if a == '1':
            School.get_list_of_classrooms(school1950)

        elif a=='2':
            School.get_students_list_of_class(school1950)

        elif a=='3':
            School.get_student_subjects(school1950)

        elif a=='4':
            print(School.get_student_parents(school1950))
        elif a=='5':
            print(School.get_teachers_of_class(school1950))

        elif a=='0':
            break
        else: print('ERROR')

school1950=School('1950')

students = [Student('ФИОуч-ка1', 'ФИОр11', 'ФИОр12', '5а'),
            Student('ФИОуч-ка2', 'ФИОр21', 'ФИОр22', '5а'),
            Student('ФИОуч-ка3', 'ФИОр31', 'ФИОр32', '5а'),
            Student('ФИОуч-ка4', 'ФИОр41', 'ФИОр42', '6а'),
            Student('ФИОуч-ка5', 'ФИОр51', 'ФИОр52', '6а'),
            Student('ФИОуч-ка6', 'ФИОр61', 'ФИОр62', '6а'),
            Student('ФИОуч-ка7', 'ФИОр71', 'ФИОр72', '7а'),
            Student('ФИОуч-ка8', 'ФИОр81', 'ФИОр82', '7а'),
            Student('ФИОуч-ка9', 'ФИОр91', 'ФИОр92', '7а'),
            Student('ФИОуч-ка10', 'ФИОр101', 'ФИОр102', '8а'),
            Student('ФИОуч-ка11', 'ФИОр111', 'ФИОр112', '8а'),
            Student('ФИОуч-ка12', 'ФИОр121', 'ФИОр122', '8а')]

teachers = [Teacher('ФИОуч-ля1', 'Предмет1', ['5а','6а','7а']),
            Teacher('ФИОуч-ля2', 'Предмет2', ['6а','7а']),
            Teacher('ФИОуч-ля3', 'Предмет3', ['6а','7а','8а']),
            Teacher('ФИОуч-ля4', 'Предмет4', ['6а','7а','8а']),
            Teacher('ФИОуч-ля5', 'Предмет5', ['7а','8а'])]


menu()