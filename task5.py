revenue = float(input('Введите выручку фирмы: '))
costs = float(input('Введите издержки фирмы: '))
result = revenue - costs
if result > 0:
    print(f'Фирма работает с Прибылью: {result}')
    profitability = result / revenue
    print(f'Рентабельность: {profitability}')
    number_of_employees = int(input('Введите количество сотрудников: '))
    profit_per_employee = result / number_of_employees
    print(f'Прибыль фирмы на одного сотрудника: {profit_per_employee}')
else:
    print(f'Фирма работает в Убыток: {result}')
