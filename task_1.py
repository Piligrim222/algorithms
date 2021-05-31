'''
Задача 1.
Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

https://drive.google.com/file/d/15VKpD1xdh_rVgVedQ_b_Oge4ACz_OnLO/view?usp=sharing
'''

Chislo = int(input("Введите трехзначное число: "))
a = int(Chislo / 100)
b = int((Chislo - a * 100) / 10)
c = int(Chislo - a * 100 - b * 10)
print(f"Сумма: {a + b + c}. Произведение: {a * b * c}")
