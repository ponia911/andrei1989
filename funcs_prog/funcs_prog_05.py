#Дан список чисел. Вернуть список,
# где каждое число переведено в строку
#[5, 3] -> [‘5’, ‘3’]


arr = [1, 2, 3, 4, 5, 6]

new_arr = list(map(str,arr))
print(new_arr)

new_arr_2 = [str(i) for i in arr]



def my_func(i):
    return str(i)


new_arr_3 = list(map(my_func, arr))
print(new_arr_3)