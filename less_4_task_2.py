"""
Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать на
вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.

Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и попробуйте его
улучшить/оптимизировать под задачу.

Второй — без использования «Решета Эратосфена».
Примечание. Вспомните классический способ проверки числа на простоту.
"""
import cProfile
import timeit

max_range = 100_000


# Вариант 1
def sieve(n):
    lst = [i for i in range(max_range)]
    lst[1] = 0
    for i in range(2, max_range):
        if lst[i] != 0:
            j = i + i
            while j < max_range:
                lst[j] = 0
                j += i
    prime_lst = [i for i in lst if i != 0]
    return prime_lst[n - 1]


print(timeit.timeit('sieve(500)', number=10, globals=globals()))  # 0.4636496
print(timeit.timeit('sieve(1000)', number=10, globals=globals()))  # 0.4779143
print(timeit.timeit('sieve(2000)', number=10, globals=globals()))  # 0.4529626000000001
print(timeit.timeit('sieve(4000)', number=10, globals=globals()))  # 0.4489223

cProfile.run('sieve(4000)')
#       6 function calls in 0.054 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.001    0.001    0.053    0.053 <string>:1(<module>)
#      1    0.043    0.043    0.052    0.052 less_4_task_2.py:19(sieve)
#      1    0.006    0.006    0.006    0.006 less_4_task_2.py:20(<listcomp>)
#      1    0.003    0.003    0.003    0.003 less_4_task_2.py:28(<listcomp>)
#      1    0.000    0.000    0.054    0.054 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# Вариант 2
def prime(n):
    prime_lst = []
    if n == 1:
        return 2
    elif n == 2:
        return 3
    for i in range(2, max_range):
        d = 2
        while d * d <= i and i % d != 0:
            d += 1
            if d * d > i:
                prime_lst.append(i)
                break
    return prime_lst[n - 3]


print(timeit.timeit('prime(500)', number=10, globals=globals()))  # 6.656787700000001
print(timeit.timeit('prime(1000)', number=10, globals=globals()))  # 6.498804999999999
print(timeit.timeit('prime(2000)', number=10, globals=globals()))  # 6.524339400000001
print(timeit.timeit('prime(4000)', number=10, globals=globals()))  # 6.653177100000001

cProfile.run('prime(4000)')

#       9594 function calls in 0.679 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.679    0.679 <string>:1(<module>)
#      1    0.678    0.678    0.679    0.679 less_4_task_2.py:40(prime)
#      1    0.000    0.000    0.679    0.679 {built-in method builtins.exec}
#   9590    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# print(f'{sieve(2)=}')
# print(f'{sieve(5)=}')
# print(f'{prime(4)=}')
# print(f'{prime(1)=}')

"""
Вывод. Оба варианта имеют константную сложность, увеличение N не влияет на время работы программ. 
Вариант 1 "Решето" предпочтительней и значительно быстрее Варианта 2. Проблемное место у 2-го варианта метод 'append', 
который во время теста вызывался 9590 раз.
"""
