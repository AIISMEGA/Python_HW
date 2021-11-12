class OwnExpection(Exception):
    def __init__(self):
        self.txt = 'Некорректный тип данных! Необходимо ввести число!'

mylist = []
input_string = input('Введите число. Для выхода введите пустую строку: ')
while input_string:
    try:
        if input_string.isdigit():
            mylist.append(int(input_string))
        else:
            raise OwnExpection
    except OwnExpection as e:
        print(e.txt)

    input_string = input('Введите число. Для выхода введите пустую строку: ')

print(mylist)