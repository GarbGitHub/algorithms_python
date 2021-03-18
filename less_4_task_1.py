"""
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""

import timeit
import cProfile

"""Вариант 1. O(N2), квадратическая асимтотика, линейная сложность
Наблюдается линейный рост затрат времени в зависимости от N"""


def fun_v1(min_1, max_1, min_2, max_2):
    for num_1 in range(min_1, max_1 + 1):
        count = 0
        for num_2 in range(min_2, max_2 + 1):
            if num_2 % num_1 == 0:
                count += 1
        # print(f'{count} чисел кратны {num_1}')


print(timeit.timeit('fun_v1(2, 9, 2, 99)', number=300, globals=globals()))      # 0.01739840000000001
print(timeit.timeit('fun_v1(2, 20, 2, 200)', number=300, globals=globals()))    # 0.07478560000000001
print(timeit.timeit('fun_v1(2, 40, 2, 400)', number=300, globals=globals()))    # 0.2736699
print(timeit.timeit('fun_v1(2, 80, 2, 800)', number=300, globals=globals()))    # 1.2343338
print(timeit.timeit('fun_v1(2, 160, 2, 1600)', number=300, globals=globals()))  # 4.7116215
print(timeit.timeit('fun_v1(2, 360, 2, 3200)', number=300, globals=globals()))  # 22.3531806
print(timeit.timeit('fun_v1(2, 720, 2, 6400)', number=300, globals=globals()))  # 91.8422897

cProfile.run('fun_v1(2, 500, 2, 100_000)')
#       4 function calls in 4.596 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    4.596    4.596 <string>:1(<module>)
#      1    4.596    4.596    4.596    4.596 less_4_task_1.py:10(fun_v1)
#      1    0.000    0.000    4.596    4.596 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


"""
Вариант 2 "Рекурсия". O(N2), квадратическая аcимтотика, предположительно линейная сложность.
Для значений n до 2, 360, 2, 3200 наблюдается примерно линейный рост затрат времени в зависимости от N.

Далее наблюдается очевидно нелинейный характер роста временных затрат. Увеличение N до крупных значений -
приведет к переполнению стека, и вызову ошибки.
"""


def fun_v2(min_1, max_1, min_2, max_2):
    len_ = len([el for el in range(min_1, max_1 + 1)])
    array = [el for el in range(min_2, max_2 + 1)]

    def calculation(num):
        count = 0
        for el in array:
            if el % num == 0:
                count += 1
        # print(f'{count} чисел кратны {num}')
        if num < len_ + 1:
            calculation(num + 1)

    calculation(min_2)


print(timeit.timeit('fun_v2(2, 9, 2, 99)', number=10, globals=globals()))       # 0.000665900000000004
print(timeit.timeit('fun_v2(2, 20, 2, 200)', number=10, globals=globals()))     # 0.0024171999999999944   (3.6)
print(timeit.timeit('fun_v2(2, 40, 2, 400)', number=10, globals=globals()))     # 0.009854299999999996    (4.1)
print(timeit.timeit('fun_v2(2, 80, 2, 800)', number=10, globals=globals()))     # 0.036815600000000004    (3.7)
print(timeit.timeit('fun_v2(2, 160, 2, 1600)', number=10, globals=globals()))   # 0.16069060000000002     (4.4!)
print(timeit.timeit('fun_v2(2, 360, 2, 3200)', number=300, globals=globals()))  # 18.0884076              (112!)
print(timeit.timeit('fun_v2(2, 720, 2, 6400)', number=300, globals=globals()))  # 75.0617744              (4.2)

cProfile.run('fun_v2(2, 500, 2, 100_000)')

#       506 function calls (8 primitive calls) in 4.019 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    4.019    4.019 <string>:1(<module>)
#      1    0.000    0.000    4.019    4.019 less_4_task_1.py:41(fun_v2)
#      1    0.000    0.000    0.000    0.000 less_4_task_1.py:42(<listcomp>)
#      1    0.005    0.005    0.005    0.005 less_4_task_1.py:43(<listcomp>)
#  499/1    4.014    0.008    4.014    4.014 less_4_task_1.py:45(calculation)
#      1    0.000    0.000    4.019    4.019 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


"""Вариант 3 "Массив" O(N2), квадратическая аcсимтотика, линейная сложность
Наблюдается линейный рост затрат времени в зависимости от N значений"""


def fun_v3(min_1, max_1, min_2, max_2):
    frequency = [0] * (max_1 - min_1 + 1)

    for i in range(min_2, max_2 + 1):
        for j in range(min_1, max_1 + 1):
            if i % j == 0:
                frequency[j - min_1] += 1

    for i, item in enumerate(frequency, start=min_1):
        pass
        # print(f'Числу {i} кратно {item} чисел')


# print('Вариант 3')
print(timeit.timeit('fun_v3(2, 9, 2, 99)', number=300, globals=globals()))      # 0.025914900000003627
print(timeit.timeit('fun_v3(2, 20, 2, 200)', number=300, globals=globals()))    # 0.08873249999999189     (3.5)
print(timeit.timeit('fun_v3(2, 40, 2, 400)', number=300, globals=globals()))    # 0.31842810000000554     (3.5)
print(timeit.timeit('fun_v3(2, 80, 2, 800)', number=300, globals=globals()))    # 1.0975151000000096      (3.5)
print(timeit.timeit('fun_v3(2, 160, 2, 1600)', number=300, globals=globals()))  # 4.18163899999999        (3.8)
print(timeit.timeit('fun_v3(2, 360, 2, 3200)', number=300, globals=globals()))  # 19.85225249999999       (4.7)
print(timeit.timeit('fun_v3(2, 720, 2, 6400)', number=300, globals=globals()))  # 88.54042660000005       (4.4)

cProfile.run('fun_v3(2, 500, 2, 100_000)')
#          4 function calls in 4.601 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    4.601    4.601 <string>:1(<module>)
#         1    4.601    4.601    4.601    4.601 less_4_task_1.py:61(fun_v3)
#         1    0.000    0.000    4.601    4.601 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#
# Process finished with exit code 0

"""Вывод:
Несмотря на то, что вариант 2 с рекурсией оказался самым быстрым, мне кажется 3 вариант более предпочтительным
(хотя есть подозрение, что в 3-м потребление памяти будет выше чем в первом). 2 вариант можно было бы использовать
с гарантированно низкими N данными, например как в условии задачи, но я исхожу из того что объем входных данных
может динамически меняться и при увеличении произойдет переполнение стека.
"""
