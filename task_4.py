"""
Задача 4.
Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.
"""

n = int(input("Введите количество членов ряда: "))
i = 1
res = 0
for _ in range(0, n):
    res += i
    i /= -2

if n != 1:
    print(f"Сумма {n} членов ряда равна {res}.")
else:
    print(f"{res}")
