"""
Задача 4.
Определить, какое число в массиве встречается чаще всего.
"""
import random

size = 10000
min_item = -1000
max_item = 1000
arr = [random.randint(min_item, max_item) for _ in range(size)]
# print(arr)

dict = {}
for i in arr:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1

max_col = 0
for i in dict:
    if dict[i] > max_col:
        max_col = dict[i]
        max = i

print(f"Число {max} встречается {max_col} раз(а).")
