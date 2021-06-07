"""
Задача 3.
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например,
если введено число 3486, надо вывести 6843.
"""


def numbers(num):
    if len(str(num)) == 1:
        return str(num)
    else:
        return str(num % 10) + numbers(num // 10)


chs = int(input("Введите натуральное число: "))
print(int(numbers(chs)))
