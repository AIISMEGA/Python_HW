def my_func(a, b, c, ):
    return a + b + c

a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))
c = float(input('Введите третье число: '))

if a > b > c:
    c = 0
if b > a > c:
    c = 0
if a > c > b:
    b = 0
if c > a > b:
    b = 0
if c > b > a:
    a = 0
if b > c > a:
    a = 0

print(my_func(a,b,c))

