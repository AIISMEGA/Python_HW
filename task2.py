time = int(input('Введите время в секундах: '))
time_hour = time // 3600
time_remains = time % 3600
time_minutes = time_remains // 60
time_seconds = time_remains % 60
print(f'{time_hour:02}:{time_minutes:02}:{time_seconds:02}')

