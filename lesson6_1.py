import time
class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']
    def running(self):
        self.__color = 'Красный'
        print(f'Светофор переключается на: {self.__color}')
        time.sleep(7)
        self.__color = 'Желтый'
        print(f'Светофор переключается на: {self.__color}')
        time.sleep(2)
        self.__color = 'Зеленый'
        print(f'Светофор переключается на: {self.__color}')
        time.sleep(5)
        while True:
            self.running()

traff_light = TrafficLight()
print(traff_light.running())