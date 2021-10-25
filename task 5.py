my_list = [7, 5, 3, 3, 2]
new_element = float(input('Введите новый элемент (натуральное число): '))
i = 0
for num in my_list:
    if new_element <= num:
        i = i+1
my_list.insert(i, int(new_element))
print(my_list)

