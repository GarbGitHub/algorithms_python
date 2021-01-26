"""
Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.
https://drive.google.com/file/d/1U5p0MkCEWTmqBH14qJDYblFtqZTmzdQl/view?usp=sharing
"""


def calculation(n, s, c):
    s = s + c
    c = c / -2
    n -= 1
    if n < 1:
        return s
    return calculation(n, s, c)


num = int(input('Введите число: '))
summa = 0
count = 1
z = (calculation(num, summa, count))
print(z)

# Без рекурсии
# n = int(input('Введите число: '))
# sum = 0
# count = 1
# for i in range(n):
#     sum = sum + count
#     count = count / -2
# print(sum)
