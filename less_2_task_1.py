"""
Написать программу, которая будет складывать, вычитать, умножать или делить два числа. Числа и знак операции
вводятся пользователем. После выполнения вычисления программа не завершается, а запрашивает новые данные для
вычислений. Завершение программы должно выполняться при вводе символа '0' в качестве знака операции. Если
пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), программа должна сообщать об ошибке и снова
запрашивать знак операции. Также она должна сообщать пользователю о невозможности деления на ноль, если он ввел его в
качестве делителя.
https://drive.google.com/file/d/1U5p0MkCEWTmqBH14qJDYblFtqZTmzdQl/view?usp=sharing
"""


def calculation(a, b, s):
    if s == '+' or s == '-' or s == '*' or s == '/' or s == '0':
        if s == '+':
            return a + b
        if s == '-':
            return a - b
        if s == '*':
            return a * b
        if s == '/' and b != 0:
            return a / b
        else:
            return 'ZeroDivisionError! Нельзя делить на 0!'
    else:
        return 'Error! Действие введено не верно!'


while True:
    try:
        print('Введите 2 числа и действие')
        num1 = float(input('a = '))
        num2 = float(input('b = '))
        act = input('действие: ')
        if act == '0':
            print('Программа завершила работу')
            break
        print(calculation(num1, num2, act))
    except ValueError:
        print('Error: ValueError!')

# упрощенно c 1-м циклом
# while True:
#     try:
#         print('Введите 2 числа и действие')
#         a = float(input('a = '))
#         b = float(input('b = '))
#         s = input('действие: ')
#         if s == '0':
#             print('Программа завершила работу')
#             break
#         if s == '+' or s == '-' or s == '*' or s == '/' or s == '0':
#             if s == '+':
#                 print(a + b)
#             elif s == '-':
#                 print(a - b)
#             elif s == '*':
#                 print(a * b)
#             else:
#                 print(a / b) if b != 0 else print("ZeroDivisionError! Нельзя делить на 0!")
#         else:
#             print("Error! Действие введено не верно!")
#
#     except ValueError:
#         print('Error: ValueError!')


# Рекурсивно
# mess = "Введите 2 числа и действие"

# def calculation(mess) -> float:
#     try:
#         print(mess)
#         a = float(input('a =  '))
#         b = float(input('b = '))
#         s = input('действие: ')
#         result = 0
#         if s == '+' or s == '-' or s == '*' or s == '/' or s == '0':
#             if s == '+':
#                 result = a + b
#             if s == '-':
#                 result = a - b
#             if s == '*':
#                 result = a * b
#             if s == '/':
#                 result = a / b if b != 0 else calculation('Делить на 0 нельзя!\n' + mess)
#             if s != '0':
#                 print(f'Результат = {result:.2f}')
#                 return calculation(mess)
#             else:
#                 print('Работа программы завершена')
#         else:
#             return calculation('Действие введено не верно!\n' + mess)
#     except ValueError:
#         return calculation('Error: ValueError!\n' + mess)
#
#
# calculation(mess)
