"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для
каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести
наименования предприятий, чья прибыль выше среднего и ниже среднего.
"""
from collections import defaultdict, deque

data = deque()
total_profit = 0
quantity_company = 0

while True:
    try:
        quantity_company = int(input('Введите количество компаний: '))
    except ValueError:
        print('ValueError: не верный тип данных')
        continue
    break

for count_company, _ in enumerate(range(quantity_company), 1):
    name_company = input(f'Введите название {count_company}-ой компании: ')

    for count_quarter, _ in enumerate(range(4), 1):
        profit = 0
        while True:
            try:
                profit = float(input(f'Введите прибыль "{name_company}" за {count_quarter}: квартал: '))
            except ValueError:
                print('ValueError: не верный тип данных')
                continue
            break
        profit_company = (name_company, profit)
        data.append(profit_company)
        total_profit += profit

company_register = defaultdict(list)

for name, profit in data:
    company_register[name].append(profit)

print(data)
print(company_register)

best_companies = deque()
mid_companies = deque()
average_profit = total_profit / quantity_company  # Средняя прибыль за год

print(f'\nСредняя прибыль за 1 год по всем компаниям {average_profit}')


for name, profit in company_register.items():
    best_companies.append(name) if sum(profit) >= average_profit else mid_companies.append(name)


print(f'Прибыль выше среднего у компаний:')
for name in best_companies:
    print(name)

print(f'Прибыль ниже среднего у компаний:')
for name in mid_companies:
    print(name)
