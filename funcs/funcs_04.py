#Реализовать функцию возвращающую матрицу.
# На вход принимает n - размерность матрицы,
# random_from(по-умолчанию 1), random_to(по-умолчанию(9)).

def create_matrix(n, random_from=1, random_to=9):
    return [[randint(random_from, random_to) for _ in range(n)] for _ in range(n)]



def create_matrix_2(n, random_from=1, random_to=9):
    matrix = []
    for _ in range(n):
        arr_in = []
        for _ in range(n):
            arr_in.append(randint(random_from, random_to))
            matrix.append(arr_in)
            return matrix

        def main():
            print(random_from)
            print(random_to)

        if __name__ == '__main__':
            main()
