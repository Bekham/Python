import time


class TrafficLight:
    __color = ['RED', 'YELLOW', 'GREEN', 'YELLOW']

    def running(self):
        stop = False
        time_mode = [7, 2, 8, 2]
        check_mode = ['RED', 'YELLOW', 'GREEN', 'YELLOW']
        while not stop:
            for mode in range(len(self.__color)):
                if self.__color[mode] == check_mode[mode]:
                    print(self.__color[mode])
                    time.sleep(time_mode[mode])
                else:
                    stop = True


t = TrafficLight()
while True:
    t.running()
