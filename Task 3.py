with open('staff.txt', 'r') as f:
    workers = {line.split()[0]: int(line.split()[1]) for line in f}
    print(f'Средняя зарплата = {round(sum(workers.values()))/len(workers)}')
    print(f'Зарплата ниже 20k {[el[0] for el in workers.items() if el[1] < 20000]}')