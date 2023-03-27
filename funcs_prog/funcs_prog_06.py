#arr = [1, 2, 3, 4, 5, 6]
#new_arr = list(filter(lambda x: x%2 == 0, arr))
#print(new_arr)

#new_arr = list(filter(lambda x: x%2, arr))
#print(new_arr)

#new_arr = list(filter(lambda x: x / 2, arr))
#print(new_arr)

#Дан список имен, отфильтровать все имена, где есть буква o

#[‘Kate’, ‘Kolya’, ‘Alex’] -> [‘Kolya’]

arr = ['Kate', 'Kolya', 'Alex']

new_arr = list(filter(lambda x: 'o' in x, arr))

def my_func(x):
    return 'o' in x

new_arr_2 = list(filter(my_func, arr))
print(new_arr_2)
