__author__ = 'Фещук Олег Анатольевич'

# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]
import math

list1=[2, -5, 8, 9, -25, 25, 4, 0]
list2=[]

for i in list1:
    if i >=0:
        if math.sqrt(i) % 1 == 0:
            list2.append(int(math.sqrt(i)))
        else: pass
    else: pass

print(list2)

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)


months = ['ошибка', 'января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября',
          'ноября','декабря']
days = ['ошибка','первое', 'второе', 'третье', 'четвёртое','пятое','шестое','седьмое','восьмое','девятое','десятое',
        'одиннадцатое', 'двенадцатое', 'тринадцатое', 'четырнадцатое', 'пятнадцатое','шестнадцатое', 'семнадцатое',
        'восемнадцатое', 'девятнадцатое', 'двадцатое','двадцать первое', 'двадцать второе','двадцать третье',
        'двадцать четвёртое','двадцать пятое', 'двадцать шестое', 'двадцать седьмое','двадцать восьмое',
        'двадцать девятое', 'тридцатое', 'тридцать первое',]

date = input('Введите дату в формате dd.mm.yyyy')

w_day = days[int(date[:2])]
w_month = months[int(date[3:5])]

w_date = w_day + ' ' + w_month + ' ' + str(date[6:] + ' года')
print(w_date)

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

import random

n = int(input('Сколько нужно чисел?'))
list3 = []
for i in range(n):
    list3.append(random.randint(-100,100))
print(list3)

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

list4 = [1, 2, 4, 5, 6, 2, 5, 2]
list5 = list(set(list4))

print(list5)
list6=[]
for i in list4:
    if list4.count(i)==1:
        list6.append(i)
print(list6)