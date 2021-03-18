"""
Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
Требуется вернуть количество различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком.
"""
import hashlib

user_txt = input('Введите текст: ')


def calculating_unique_hash_strings(txt):
    size_txt = len(txt)
    h_set = set()  # set содержит только уникальные элементы

    for i in range(size_txt):
        size_txt = len(txt) - 1 if i == 0 else len(txt)
        for j in range(size_txt, i, -1):
            h_set.add(hashlib.sha1(txt[i:j].encode('utf-8')).hexdigest())
    # print(h_set)
    return f'Количество уникальных подстрок: {len(h_set)}'


print(calculating_unique_hash_strings(user_txt))
