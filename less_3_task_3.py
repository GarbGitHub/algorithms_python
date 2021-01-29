"""
Определить, какое число в массиве встречается чаще всего.
"""

import random

SIZE = 1_000
MIN_ITEM = 0
MAX_ITEM = 100_000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

x = 0
num = None
for el1 in array:
    count = 0
    for el2 in array:
        if el2 == el1:
            count += 1
    if count > x:
        x = count
        num = el1
if x == 1:
    print('все числа в массиве записаны по 1 разу')
else:
    print(f'Число {num} встречается {x} раз')
