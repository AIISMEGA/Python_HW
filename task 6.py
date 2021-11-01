from itertools import count, cycle

for i in count(3):
    print(i)
    if i == 10:
        break
count = 0
for el in cycle([1, 2, 3]):
    count += 1
    if count == 10:
        break
    print(el)
