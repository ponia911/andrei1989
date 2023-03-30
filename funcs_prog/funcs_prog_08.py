#Написать декоратор, который будет выводить время
# выполнения функции
from datetime import datetime
time = datetime.now()
#from  import datetime


def my_decoratore(func):
    @raps(func)
    def ineer(*args, **kwargs):
        start_time = datetime.now()
        result = func()
        finish_time = datetime.now()
        delta = finish_time - start_time
        print(delta)
        return result
    return ineer

@my_decoratore

def very_importent_func(arr):
    from time import sleep
    arr = list(map(lambda x: x * 2, arr))
    print(arr)
    return arr

def main():
    arr = [i for i in range(100)]
