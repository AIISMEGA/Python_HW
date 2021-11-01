from itertools import count
from math import factorial

def fact():
    for el in count(1):
        yield factorial(el)

generator = fact()
a = 0

for i in generator:
    if a == 10:
        break
    else:
        a+=1
        print(f'Факториал {a} = {i}')

