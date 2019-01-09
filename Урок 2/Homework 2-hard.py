__author__ = 'Фещук Олег Анатольевич'

# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

equation = 'y = -12x + 11111140.2121'
x = 2.5

# вычислите и выведите y

k=float(equation[4:'y = -12x + 11111140.2121'.find('x')])
b=float(equation[('y = -12x + 11111140.2121'.find('x')+4):])

y=k*x+b
print(y)

# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
date = '01.11.1985'

# Примеры некорректных дат
date = '01.22.1001'
date = '1.12.1001'
date = '-2.10.3001'

date = input('date')

if date[2] != '.':
    print('format_error')
if date[5] != '.':
    print('format_error')


ds = date.split(date[2])


if len(ds[0]) != 2:
    print('error_day')
if len(ds[1]) != 2:
    print('error_month')
if len(ds[2]) != 4:
    print('error_year')

day = int(ds[0])
month = int(ds[1])
year = int(ds[2])

month31 = [1, 3, 5, 7, 8, 10, 12]

if month not in month31:
    if day < 31:
        if day > 0:
            print('day_ok')
        else: print('error_day')
    else: print('error_day')
if month in month31:
    if day < 32:
        if day > 0:
            print('day_ok')
        else: print('error_day')
    else: print('error_day')
if month > 0:
    if month <= 12:
        print('month_ok')
    else: print('error_month')
else: print('error_month')

if year > 0:
    if year < 10000:
        print('year_ok')
    else: print('error_year')
else: print('error_year')

# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты,
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3
n=0
while n not in range(1,2000001):
    n = int(input('Room number:'))
    if n not in range(1,2000001):
        print('room does not exist')

room_q = 1
floor_w = 0

sofb = 0                           # squares of floor sizes before

while n > sofb:
    sofb = sofb + room_q ** 2
    room_q = room_q + 1
    floor_w=floor_w+1

room_q = room_q-1

lrps = sofb-room_q**2             # last room of previous stage
pslf = room_q/2*(room_q-1)        # previous stage last floor
rnws = n-lrps                     # room number within stage

n_floor = int(pslf+rnws//floor_w+1)
n_row = rnws % floor_w

if n_row == 0:
    n_row = floor_w
    n_floor = n_floor-1

n_floor = str(n_floor)+','

print('Ответ:')
print('Этаж №',n_floor,'в',n_row,'ряду слева.')