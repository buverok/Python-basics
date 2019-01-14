__author__ = 'Фещук Олег Анатольевич'

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    number=str(number)
    x=number.find('.')
    if int(number[x+ndigits+1]) >= 5:
        number = float(number) * (10 ** ndigits)+1
    else: number = float(number) * (10 ** ndigits)

    number=number/(10**ndigits)
    number=str(number)
    number=number[0:x+ndigits+1]
    return float(number)

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    ticket_number=str(ticket_number)
    a1=int(ticket_number[0])
    a2=int(ticket_number[1])
    a3=int(ticket_number[2])
    a4=int(ticket_number[3])
    a5=int(ticket_number[4])
    a6=int(ticket_number[5])
    if (a1+a2+a3) == (a4+a5+a6):
        return 'Luck'

print(lucky_ticket(123006))
print(lucky_ticket(123215))
print(lucky_ticket(436751))