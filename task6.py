jogging_first_day = float(input('Введите количество километров пробега в первый день: '))
final_result = float(input('Введите целевое значение пробега в километрах: '))
if jogging_first_day == final_result:
    print(1)
else:
    mileage = jogging_first_day
    day = 1
    while mileage < final_result:
        mileage += (mileage / 100) * 10
        day += 1
    print(day)

