#Создать декоратор для функции,
# которая принимает список чисел.
# Декоратор должен производить предварительную проверку данных -
# удалять все четные элементы из списка.

def my_decorator(func):

    #@raps
    def inner(arr):
        arr = [i for i in arr if i % 2]
        result = func(arr)
        return result

    return inner


@my_decorator
def my_func_2(arr):
    print(arr)
    return arr, len(arr)



arr =[i for  i in range(1, 20)]
print(my_func_2(arr))
#a = my_func(arr)
#print(a)
b = my_func_2(arr)
print(b)
