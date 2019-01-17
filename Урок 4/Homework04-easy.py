__author__ = 'Фещук Олег Анатольевич'

# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

import random

list = [random.randint(-10, 10) for _ in range(5)]
print(list)
list2=[x**2 for x in list]
print(list2)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruits1 = ['banana', 'apple', 'orange', 'melon', 'pear', 'pomelo']
fruits2=['grapefruit', 'pineapple','apple', 'watermelon', 'orange', 'pomelo']
fruits3=[x for x in fruits1 if x in fruits2]

print(fruits3)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

list = [random.randint(-100, 100) for _ in range(20)]
print(list)
list2 = [x for x in list if x%3==0 and x>0 and x%4!=0]
print(list2)