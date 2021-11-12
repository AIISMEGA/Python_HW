class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def extract_data(cls, date):
        try:
            day, month, year = date.split("-")
            return int(day), int(month), int(year)
        except Exception as e:
            print(f'Не удалось выделить дату из строки! {e}')

    @staticmethod
    def validate_data(date_input):
        try:
            day, month, year = date_input
            if day not  in range(1, 32):
                raise ValueError('День указан некорректно!')
            elif month not in range(1,13):
                raise ValueError('Месяц указан некорректно!')
            elif year not in range(0,2040):
                    raise ValueError('Год указан некорректно!')
        except ValueError as e:
            print(e)
        else:
            print('Дата проверена успешно!')


my_data_cls = Date('15-11-2021')
my_date = my_data_cls.extract_data(my_data_cls.date)
print(my_date)
if my_date:
    my_data_cls.validate_data(my_date)