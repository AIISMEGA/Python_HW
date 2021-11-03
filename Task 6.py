dictionary = {}
with open('lessons.txt', encoding= 'utf -8') as f:
    for line in f:
        name, lessons = line.split(':')
        elem = [i for i in lessons if i == ' ' or (i >= '0' and i <='9')]
        name_sum = sum(map(int,"".join(elem).split()))
        dictionary[name] = name_sum
print(dictionary)