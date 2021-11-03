with open('data.txt', 'r') as f:
    quantity = ([f'{num}.{" ".join(line.split())} - {len(line.split())} слов' for num, line in enumerate(f, 1)])
    print(quantity, f'строк: {len(quantity)}', sep='\n')