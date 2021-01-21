"""
Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
https://drive.google.com/file/d/1LNKYIAR-qy9HLNaE2lWW3VSjccE5I75x/view?usp=sharing
"""

num = int(input('Номер буквы в алфавите: '))

if num < 1:
    print('Число должно быть больше 0')
elif num > 26:
    print('Число должно быть меньше 27')
else:
    num = ord('a') + num - 1
    print(f'Найдена буква {chr(num)}')
