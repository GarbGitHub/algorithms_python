"""
 Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
 Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
 медианы, в другой — не больше медианы.

Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно, используйте метод
сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).
"""

import random

m = 5  # в массиве с нечетной величиной, m - является серединой
SIZE = 2 * m + 1
MIN = 1
MAX = 20
array = [random.randint(MIN, MAX) for _ in range(SIZE)]


def gnome_sort(data):
    i = 1
    size = len(data)
    while i < size:
        if data[i - 1] <= data[i]:
            i += 1
        else:
            data[i - 1], data[i] = data[i], data[i - 1]
            if i > 1:
                i -= 1
    return data


print('Массив до сортировки:')
print(array)

print('\nМассив после сортировки:')
array_sorted = (gnome_sort(array))
print(array_sorted)
print(f'\nМедиана: "index": {m}, "value": {array_sorted[m]}')


# :-( Чебурашка где-то рядом
# def func(data):
#     for i in range(len(data)):
#         count_max = 0
#         count_min = 0
#         for j in range(len(data)):
#             if data[i] >= data[j]:
#                 count_max += 1
#             if data[i] <= data[j]:
#                 count_min += 1
#             # if data[i] == data[j]:
#             #     pass
#         if count_min == count_max:
#             return {"index": [i], "value": data[i]}
