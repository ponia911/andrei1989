#Написать программу для работы с матрицами:
#Создание
#Вывод
#Сумма всех элементов
#Нахождение максимального элемента
#Нахождение минимального элемента.

from random import randint

#matrix = [[randint(1, 10) for _  in range(n) for _ in range(n)]]
def create_matrix(n):
    arr = []
        for i in range(n):
                arr_in = []
                for i in range(n):

                    arr_in.append(randint(0, 9))

                    matrix.append(arr_in)
                return matrix
        print(arr)

    for arr in matrix:
        result += sum(arr)
        result = sum([sum(arr) for arr in matrix])
        return result

def max_element(matrix):
    list_of_max_element = []
     for arr in matrix:
        max_element_in
