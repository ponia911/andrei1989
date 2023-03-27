#Дан список чисел.
# Найти произведение всех чисел, которые кратны 3.
from functools import reduce

arr = [i for  i in range(10)]
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_arr = [i for i in arr if i % 3 == 0]
print(new_arr)

# version 2
new_arr = filter(lambda x, y: x * y, filter(lambda x: x % 3 == 0, arr))
result = reduce(lambda x, y: x * y, new_arr)
print(result)

result = reduce(lambda x, y: x * y, filter(lambda x: x % 3 == 0, new_arr))
print(result)

#version 3


result = reduce(lambda x, y: x * y, filter(lambda x: x% 3 == 0, arr))
print(result)
