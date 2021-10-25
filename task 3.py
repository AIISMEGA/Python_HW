calendar = int(input('Введите номер месяца года: '))
months_1 = [12, 1, 2, 'зима']
months_2 = [3, 4, 5, 'весна']
months_3 = [6, 7, 8, 'лето']
months_4 = [9, 10, 11, 'осень']
if calendar == 12 or calendar == 1 or calendar == 2:
    print(months_1[3])
elif calendar == 3 or calendar == 4 or calendar == 5:
    print(months_2[3])
elif calendar == 6 or calendar == 7 or calendar == 8:
    print(months_3[3])
else:
    print(months_4[3])

months_5 = {12: 'зима', 1: 'зима', 2: 'зима'}
months_6 = {3: 'весна', 4: 'весна', 5: 'весна'}
months_7 = {6: 'лето', 7: 'лето', 8: 'лето'}
months_8 = {9: 'осень', 10: 'осень', 11: 'осень'}
if calendar == 12 or calendar == 1 or calendar == 2:
    print(months_5.get(12))
elif calendar == 3 or calendar == 4 or calendar == 5:
    print(months_6.get(3))
elif calendar == 6 or calendar == 7 or calendar == 8:
    print(months_7.get(6))
else:
    print(months_8.get(9))
