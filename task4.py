number = int(input('Введите целое положительное число: '))
number_copy = number
maximum_digit = number % 10
while number > 0:
    digit = number % 10
    if digit > maximum_digit:
        maximum_digit = digit
    number = number // 10
print(f'Самая большая цифра в числе {number_copy} равна {maximum_digit}')
