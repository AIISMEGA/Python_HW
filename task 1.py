def function(a, b):
    return (a / b)


number_1 = float(input('Введите первое число: '))
number_2 = float(input('Введите второе число, не равное "0": '))
while number_2 == 0:
        print('Второе число не может равняться "0", введите заново')
        number_2 = float(input('Введите второе число, не равное "0": '))

print(function(number_1,number_2))

