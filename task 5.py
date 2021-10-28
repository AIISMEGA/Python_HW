def total():
    sum_number = 0
    while True:
        line = input('Введите числа через пробел, для выхода нажмите q: ').split()
        for num in line:
            if num == 'q':
                return sum_number
            else:
                sum_number += int(num)
        print(f'Сумма чисел: {sum_number}')


print(total())

