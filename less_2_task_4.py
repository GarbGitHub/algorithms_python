"""
В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток.
После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число, чем то, что загадано.
Если за 10 попыток число не отгадано, вывести правильный ответ.
https://drive.google.com/file/d/1U5p0MkCEWTmqBH14qJDYblFtqZTmzdQl/view?usp=sharing
"""

from random import randint

secret = randint(0, 100)
count = 10
mes1 = 'Загаданное число больше введенного'
mes2 = 'Загаданное число меньше введенного'

while count != 0:
    try:
        n = int(input('Введите число: '))
        count -= 1
        if n == secret:
            print(f'Вы угадали {secret=}')
            break
        elif count == 0:
            print(f'Вы проиграли! {secret=}')
        else:
            print(mes1) if secret > n else print(mes2)
    except ValueError:
        print('Допущена ошибка ввода, повторите ввод')
