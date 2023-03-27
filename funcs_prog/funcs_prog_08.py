#Написать декоратор, который будет выводить время
# выполнения функции
from datetime import datetime
time = datetime.now()



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