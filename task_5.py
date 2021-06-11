"""
Задача 5.
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.
"""

import random

size = 20
min_item = -100
max_item = 100
arr = [random.randint(min_item, max_item) for _ in range(size)]
print(arr)

max = 0
for i in range(len(arr)):
    if arr[i] < 0 and (arr[i] > arr[max] or arr[max] >= 0):
        max = i

print(f"Индекс {max}, значение {arr[max]}.")
