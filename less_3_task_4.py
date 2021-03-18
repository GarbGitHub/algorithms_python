"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

import random

SIZE = 10_000
MIN_ITEM = 0
MAX_ITEM = 100_000_000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

index_max = 0
num_max = 0
index_min = 0

print(array)

for el1 in array:
    if el1 > num_max:
        num_max = el1
        index_max = array.index(el1)

num_min = num_max

for el2 in array:
    if el2 < num_min:
        num_min = el2
        index_min = array.index(el2)

array[index_max], array[index_min] = array[index_min], array[index_max]

print(array)
