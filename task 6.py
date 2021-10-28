def int_func():
    word = input('Введите слово состоящее из маленьких латинских букв или строку из слов состоящих из маленьких латинских букв и разделенных пробелом: ')
    s = 'qwertyuioplkjhgfdsazxcvbnm'
    for i in word:
        if i in s:
            return word.title()
print(int_func())
