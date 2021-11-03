translation = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('numbers_1.txt', 'w', encoding='utf-8') as n:
    with open('numbers.txt', 'r', encoding='utf-8') as n_1:
        n.write(str([line.replace(line.split()[0], translation.get(line.split()[0])) for line in n_1]))
