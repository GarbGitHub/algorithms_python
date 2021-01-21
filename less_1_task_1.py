"""
Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
https://drive.google.com/file/d/1LNKYIAR-qy9HLNaE2lWW3VSjccE5I75x/view?usp=sharing
"""

a = int(input('введите целое натуральное трехзначное число: '))

b = a // 100
c = (a // 10) % 10
d = a % 10

e = b + c + d
f = b * c * d

print(f'Сумма цифр = {e}, Произведение цифр = {f}')
