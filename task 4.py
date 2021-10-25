user_list = input('Введите строку из нескольких слов разделённую пробелами: ').split()
for i, word in enumerate(user_list, 1):
    print(f'{i}. {word[:10]}')

