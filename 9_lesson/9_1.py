import time
import itertools


class TrafficLight:
    __color = [['Red', [7,31]], ['Yellow', [2,33]], ['Green', [7,32]]]

    def running(self):
        for ligth in itertools.cycle(self.__color):
            print(f"\r\033[{ligth[1][1]}m\033[1m{ligth[0]}\033[0m", end='')
            time.sleep(ligth[1][0])

New_TrafficLight = TrafficLight()
New_TrafficLight.running()