#Создать функцию, которая принимает на вход
# неопределенное количество аргументов
# и возвращает их сумму и максимальное из них


def sum_and_max(*args):
    return sum(args), max(args)


def main():
    result = sum_and_max(1, 1, 1, 1, 1, 10)
    print(result, type(result))
    sum, max_elem = sum_and_max(1, 1, 1, 1, 1, 10)
    print(f'sum = {sum}, max_elem = {max_elem}')

if __name__ == '__main__':
   main()