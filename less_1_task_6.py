"""
Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
https://drive.google.com/file/d/1LNKYIAR-qy9HLNaE2lWW3VSjccE5I75x/view?usp=sharing
"""

n_1 = ord(input('Введите 1-ю букву: '))
n_2 = ord(input('Введите 2-ю букву: '))

n_1 = n_1 - ord('a') + 1
n_2 = n_2 - ord('a') + 1

print(f'Позиции: {n_1}, {n_2}')
print(f'Интервал: {abs(n_1 - n_2) - 1}')
