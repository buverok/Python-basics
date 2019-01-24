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
    def __init__(self, name, classroom):
        self.name=name
        self.classroom=classroom

class Subject:
    def __init__(self, subject, teacher):
        self.subject=subject
        self.teacher=teacher

    def get_teacher(self):
        return self.teacher

class Classroom:
    def __init__(self, number):
        self.number=number

class Teacher(Person):
    def __init__(self, name, subject):
        self.name=name
        self.subject = subject

    def get_subj(self):
        return self.subject

class Student(Person):
    def __init__(self, name, parent1, parent2, classroom):
        self.name = name
        self.parent1=parent1
        self.parent2=parent2
        self.classroom=classroom

    def get_classroom(self):
        return self.classroom

    def get_parents(self):
        return self.parent1, self.parent2

    def get_name(self):
        return self.name


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

teachers = [Teacher('ФИОуч-ля1', 'Предмет1'),
            Teacher('ФИОуч-ля2', 'Предмет2'),
            Teacher('ФИОуч-ля3', 'Предмет3'),
            Teacher('ФИОуч-ля4', 'Предмет4'),
            Teacher('ФИОуч-ля5', 'Предмет5')]

subjects=[Subject('Предмет1', 'ФИОуч-ля2'),
          Subject('Предмет2', 'ФИОуч-ля4'),
          Subject('Предмет3', 'ФИОуч-ля1'),
          Subject('Предмет4', 'ФИОуч-ля3'),
          Subject('Предмет5', 'ФИОуч-ля5')]

cl = set([s.get_classroom() for s in students])

print(cl)

cl_r='6а'

st_list = [Student.get_name() for Student in students if Student.get_classroom() == cl_r]

print(st_list)

