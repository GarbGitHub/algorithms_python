"""
Написать программу сложения и умножения* двух шестнадцатеричных чисел. При этом каждое число представляется как
коллекция, элементы которой — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’,
‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’,
‘E’].
"""

# Буквы A, B, C, D, E, F имеют значения 10**10, 11**10, 12**10, 13**10, 14**10, 15**10 соответственно.

from collections import deque

dict_data = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
             'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
             0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
             10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

num_1 = deque(input('Введите 1-е шестнадцатеричное число: ').upper())
num_2 = deque(input('Введите 2-е шестнадцатеричное число: ').upper())

base = 16
memory = 0
len_ = 0
result = deque()

if len(num_1) < len(num_2):
    num_1, num_2 = num_2, num_1
    len_ = len(num_1)
else:
    len_ = len(num_2)

while len_ > 0:
    el_num_1 = num_1.pop()
    if len(num_2) > 0:
        el_num_2 = num_2.pop()
    else:
        el_num_2 = '0'  # если в маленьком числе закончились символы - присваиваем 0

    sum_ = dict_data[el_num_1] + dict_data[el_num_2] + memory
    memory = 0

    if sum_ < 10:
        result.appendleft(dict_data[sum_])
    elif sum_ >= base:
        sum_ -= base + memory
        result.appendleft(sum_)
        memory = 1
    else:
        result.appendleft(dict_data[sum_])
    len_ -= 1

print(*result, sep='')
