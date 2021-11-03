from random import randint
with open('number_2.txt',mode='w+') as f:
    f.write(' '.join([str(randint(1,50)) for i in range(100)]))
    f.seek(0)
    print(sum(map(int, f.read().split())))