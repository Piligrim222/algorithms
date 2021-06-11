"""
Задача 3.
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

import random

size = 10
min_item = 0
max_item = 100
arr = [random.randint(min_item, max_item) for _ in range(size)]
print(arr)

min_el = 0
max_el = 0

for i in range(len(arr)):
    if arr[i] < arr[min_el]:
        min_el = i
    if arr[i] > arr[max_el]:
        max_el = i

if arr.count(arr[min_el]) > 1 or arr.count(arr[max_el]) > 1:
    print("-Ну не шмогла я, не шмогла, понимаешь!")

arr[min_el], arr[max_el] = arr[max_el], arr[min_el]

print(arr)
