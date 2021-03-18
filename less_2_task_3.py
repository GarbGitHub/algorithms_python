"""
 Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
 Например, если введено число 3486, надо вывести 6843
 https://drive.google.com/file/d/1U5p0MkCEWTmqBH14qJDYblFtqZTmzdQl/view?usp=sharing
"""


def calculation(n1, n2=0) -> int:
    n2 = n2 * 10 + n1 % 10
    n1 //= 10
    if n1 == 0:
        return n2
    return calculation(n1, n2)


num = int(input('Введите число: '))
z = calculation(num)
print(z)
