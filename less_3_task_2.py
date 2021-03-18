"""
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""

array = [el for el in range(2, 100)]

for i1 in [el for el in range(2, 10)]:
    count = 0
    for i2 in array:
        if i2 % i1 == 0:
            count += 1
    print(f'{count} чисел кратны {i1}')
