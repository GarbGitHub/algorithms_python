"""
Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
https://drive.google.com/file/d/1U5p0MkCEWTmqBH14qJDYblFtqZTmzdQl/view?usp=sharing
"""

num = int(input('Введите число: '))
ch = 0
nch = 0
while num > 0:
    if num % 2 == 0:
        ch += 1
    else:
        nch += 1
    num //= 10
print(f'Четных {ch}, нечетных {nch}')
