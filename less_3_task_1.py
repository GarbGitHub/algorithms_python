"""Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями 8,
3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля), т.к. именно в
этих позициях первого массива стоят четные числа. """

import random

SIZE = 10_000
MIN_ITEM = 0
MAX_ITEM = 100_000_000
array_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
array_2 = [array_1.index(i) for i in array_1 if i % 2 == 0]
print(array_2)
