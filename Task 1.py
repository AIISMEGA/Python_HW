with open('new.txt', 'w' ) as f:
    while True:
        string = input('Введите данные или пустую строку если хотите завершить программу: ')
        if not string:
            break
        f.write(string)