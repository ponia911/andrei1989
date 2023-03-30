#Дан список строк.
# Отформатировать все строки в формате ‘{i} - {string}’,
# где i это порядковый номер строки в списке.
# Использовать генератор списков.


arr = ['qwer', 'asdf', 'zxcv']
new_arr = [f'{i} - {string}' for i, string in enumerate(arr)]
print(new_arr)

