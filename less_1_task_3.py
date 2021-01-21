"""
Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
https://drive.google.com/file/d/1LNKYIAR-qy9HLNaE2lWW3VSjccE5I75x/view?usp=sharing
"""

a = int(input('введите первое целое число: '))
b = int(input('введите второе целое число: '))
c = int(input('введите третье целое число: '))

if b < a < c:
    print(f'Среднее число {a}')
else:
    if c < a < b:
        print(f'Среднее число {a}')
    else:
        if a < b < c:
            print(f'Среднее число {b}')
        else:
            if c < b < a:
                print(f'Среднее число {b}')
            else:
                print(f'Среднее число {c}')
