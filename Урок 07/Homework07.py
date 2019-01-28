#!/usr/bin/python3

"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87
      16 49    55 77    88
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html
"""

import random
End_Game=0
ballsleft = 90
p1left = 15
p2left = 15
check=0

balls = random.sample(range(1,91), 90)
card= random.sample(range(1,91), 15)

p1numbers = random.sample(balls, 15)
p2numbers = random.sample(balls, 15)

p1_card = [p1numbers[:5], p1numbers[5:10], p1numbers[10:]]
p2_card = [p2numbers[:5], p2numbers[5:10], p1numbers[10:]]

for i in p1_card:
    i.sort()
    for x in range(4,8):
        i.insert(random.randint(0, x), ' ')
for i in p2_card:
    i.sort()
    for x in range(4,8):
        i.insert(random.randint(0, x), ' ')

def print_card_of_pl1():
    print('||||||||----Карточка игрока----||||||||')
    for i in range(3):
        print(p1_card[i])
    print('_______________________________________')

def print_card_of_pl2():
    print('||||||----Карточка компьютера----||||||')
    for i in range(3):
        print(p2_card[i])
    print('_______________________________________')

def next_ball():
    x=balls.pop(0)
    print('Выпало число:',x)
    print('Осталось',len(balls),'бочонков')
    return x

def check_the_number(x):
    for z in range(3):
        if x in p1_card[z]:
            y=p1_card[z].index(x)
            p1_card[z].remove(x)
            p1_card[z].insert(y,'X')
            print_card_of_pl1()

def check_the_number_comp(x):
    for z in range(3):
        if x in p2_card[z]:
            y=p2_card[z].index(x)
            p2_card[z].remove(x)
            p2_card[z].insert(y,'X')
            print_card_of_pl2()
            zzz=1
            return zzz
        zzz=0
        return zzz

def check_winner():
    if p2left==0:
        print('Комп победил')
    if p1left==0:
        print('Ваша ПОБЕДА!')

print_card_of_pl1()
print_card_of_pl2()


while len(balls)!=0 and End_Game!=1:
    n=next_ball()
    check=0
    print('1.Зачеркнуть число')
    print('2.Давай дальше')
    print('0.Прервать')
    a=int(input('Ваше действие?'))
    if a == 0:
        End_Game = 1
        print('Пока')
    elif a==1:
        for z in range(3):
            if n in p1_card[z]:
                check_the_number(n)
                check+=1
                p1left -= 1
            if check==0:
                print('Жулик! Игра окончена')
                End_Game = 1
                break
    elif a==2:
        for z in range(3):
            if n in p1_card[z]:
                check += 1
                if check > 0:
                    print('Игра окончена. Надо быть внимательнее')
                    End_Game = 1
            else: 'Идем дальше'
    else: print('Error')

    check_the_number_comp(n)
    for z in range(3):
        if n in p2_card[z]:
            p2left-=1
    print_card_of_pl1()
    print_card_of_pl2()
    check_winner()




