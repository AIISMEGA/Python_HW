from time import sleep

class TrafficLights:
    _color = "Черный"

    def running(self):
        while True:
            print('Красный')
            sleep(7)
            print('Желтый')
            sleep(2)
            print('Зеленый')
            sleep(7)
            print('Желтый')
            sleep(2)

trafficLights = TrafficLights()
trafficLights.running()