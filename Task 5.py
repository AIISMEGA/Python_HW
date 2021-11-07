class Stationary:

    def __init__(self, title='Рисование'):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки! {self.title}')


class Pen(Stationary):
    def draw(self):
        print(f'Рисование ручкой {self.title})')


class Pencil(Stationary):
    def draw(self):
        print(f'Рисование карандашом {self.title}')


class Marker(Stationary):
    def draw(self):
        print(f'Рисование маркером {self.title}')

stat = Stationary()
stat.draw()

mark = Marker()
pen = Pencil()

mark.draw()
pen.draw()