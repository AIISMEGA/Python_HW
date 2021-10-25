user_list = []
quantity = int(input('Введите количество элементов в списке: '))
while True:
    meaning = input('Введите элемент списка: ')
    user_list.append(meaning)
    if len(user_list) == quantity:
        break
print(user_list)
for i in range(1, len(user_list), 2):
    user_list[i-1], user_list[i] = user_list[i], user_list[i-1]
print(user_list)
