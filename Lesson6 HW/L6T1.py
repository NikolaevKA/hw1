import time

def countdown(num_of_secs):
    while num_of_secs:
        m, s = divmod(num_of_secs, 60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)
        print(min_sec_format)
        time.sleep(1)
        num_of_secs -= 1


class TrafficLight:
    # атрибуты класса
    def __init__(self):
     self.__color = "red"

    # методы класса
    def running(self):
        print("\033[31m","red")
        countdown(7)
        print("\033[33m","yellow")
        countdown(2)
        print("\033[32m","green")
        countdown(10)

a=TrafficLight()
a.running()