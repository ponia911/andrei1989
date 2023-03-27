#Дан список чисел.
# Найти произведение всех чисел, которые кратны 3.
import reduce
arr = []

result = reduce(lambda x, y: x + y, arr, 1)
print(result)