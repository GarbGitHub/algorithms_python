"""
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти. Примечание: По
аналогии с эмпирической оценкой алгоритмов идеальным решением будет:

● выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
● написать 3 варианта кода (один у вас уже есть);
● проанализировать 3 варианта и выбрать оптимальный;
● результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в файл с
кодом. Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
● написать общий вывод: какой из трёх вариантов лучше и почему.

Надеемся, что вы не испортили программы, добавив в них множество sys.getsizeof после каждой переменной, а проявили
творчество, фантазию и создали универсальный код для замера памяти."""

# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

import sys
from collections import deque


# Вариант 1
def version_1(num: int) -> str:
    size_spam = None
    size_num = 0
    even = 0
    odd = 0
    while num > 0:
        spam = num % 2
        if size_spam is None:  # Служебная проверка для разового замера "spam" и "num" до уменьшения в цикле
            size_num = num
            size_spam = spam
        if spam == 0:
            even += 1
        else:
            odd += 1
        num //= 10

    # Потребляемая память
    total_memory = sum((sys.getsizeof(size_num),
                        sys.getsizeof(even),
                        sys.getsizeof(odd),
                        sys.getsizeof(size_spam)
                        ))

    return f'Четных: {even} \t Нечетных: {odd} \t Память: {total_memory} байт'


# Вариант 2
def version_2(num: str) -> str:
    size_spam = None
    num = deque(num)
    even = []  # ! 24228 байт
    odd = []   # ! 24228 байт

    while num:
        spam = int(num.pop())
        if size_spam is None:  # Служебная проверка для разового замера "spam"
            size_spam = spam
        if spam % 2 == 0:
            even.append(spam)
        else:
            odd.append(spam)
    count_even = len(even)
    count_odd = len(odd)

    # Потребляемая память
    total_memory = sum((sys.getsizeof(num),
                        sys.getsizeof(even),
                        sys.getsizeof(odd),
                        sys.getsizeof(size_spam),
                        sys.getsizeof(count_even),
                        sys.getsizeof(count_odd)
                        ))

    return f'Четных: {count_even} \t Нечетных: {count_odd} \t Память: {total_memory} байт'


# Вариант 3
def version_3(num: str) -> str:
    size_spam = None
    num = deque(num)
    even = ''  # 5846 байт, много но меньше чем у списков
    odd = ''   # 5905 байт
    while num:
        spam = int(num.pop())
        if size_spam is None:  # Служебная проверка для разового замера "spam"
            size_spam = spam
        if spam % 2 == 0:
            even += str(spam)
        else:
            odd += str(spam)

    count_even = len(even)
    count_odd = len(odd)

    # Потребляемая память
    total_memory = sum((sys.getsizeof(num),
                        sys.getsizeof(even),
                        sys.getsizeof(odd),
                        sys.getsizeof(size_spam),
                        sys.getsizeof(count_even),
                        sys.getsizeof(count_odd)
                        ))

    return f'Четных: {count_even} \t Нечетных: {count_odd} \t Память: {total_memory} байт'


# Для замеров
ITEM = 1000000234232355543667457457547577777777**300

print(version_1(int(ITEM)))
print(version_2(str(ITEM)))
print(version_3(str(ITEM)))

# Ввод данных по условию задачи
# print(version_1(int(input('Введите число: '))))
# print(version_2(input('Введите число: ')))
# print(version_3(input('Введите число: ')))

"""
Замеры проводились:
ОС Win 10X64 / Python 3.8.6 32 bit

Вывод: первый вариант показал лучший (экономичный) результат по потреблению памяти при больших и малых входящих данных. 
Второй вариант оказался самым неэффективным, в основном из-за использования списков list.
"""
