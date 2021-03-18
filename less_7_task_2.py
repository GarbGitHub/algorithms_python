"""
Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке
 [0; 50). Выведите на экран исходный и отсортированный массивы.
"""

import random


def merge_sort(data):
    if len(data) <= 1:
        return data
    mid = int(len(data) / 2)
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])
    return merge(left, right)


def merge(left, right):
    i = 0
    j = 0
    result = []
    while i < len(left) or j < len(right):
        if not i < len(left):
            result.append(right[j])
            j += 1
        elif not j < len(right):
            result.append(left[i])
            i += 1
        elif left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    return result


SIZE = 10
MIN: float = 0
MAX: float = 50
array = [random.uniform(MIN, MAX - 0.1) for _ in range(SIZE)]
print('Исходный массив:')
print(array)
print('\nОтсортированный массив:')
print(merge_sort(array))
