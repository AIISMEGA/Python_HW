class Road:
    def __init__(self,length, width):
        self._length = length
        self._width = width

    def calculation_of_mass(self):
        return f'{self._width} м * {self._length} м * 25 кг * 5 см = {(self._length * self._width * 25 * 5)/1000} т'


road_1 = Road(5000, 20)
print(road_1.calculation_of_mass())