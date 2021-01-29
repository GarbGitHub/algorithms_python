"""В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать."""

import random

SIZE = 1_000
MIN_ITEM = 0
MAX_ITEM = 100_000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

index_max = 0
num_max = 0
index_min = 0
sum_ = 0

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

if index_max < index_min:
    for el3 in range(index_max + 1, index_min):
        sum_ += array[el3]
else:
    for el4 in range(index_min + 1, index_max):
        sum_ += array[el4]

print(sum_)
