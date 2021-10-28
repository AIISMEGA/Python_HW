"""Два варианта решения"""

"""Первый вариант"""
def my_func(x, y):
    return x ** y


x = float(input('Введите действителное положительное число: '))
y = int(input('Введите целое отрицательное число: '))
print(my_func(x,y))

"""Второй вариант"""
def my_func(x, y):
    degree = 1
    for i in range(abs(y)):
        degree *= x
    degree_is_negative = 1 / degree
    return degree_is_negative

x = float(input('Введите действителное положительное число: '))
y = int(input('Введите целое отрицательное число: '))
print(my_func(x, y))

