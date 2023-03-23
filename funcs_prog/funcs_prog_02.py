#Дан список слов. Сгенерировать новый список с перевернутыми словами

my_str = 'asdd assd assd assd assd Andrei'
list_my_str = my_str.split()
new_list_my_str = [i[::-1] for  i in list_my_str]
my_new_str = ''.join(new_list_my_str)
print(my_new_str)

arr = ['asdd', 'assd', 'assd', 'assd', 'assd', 'Andrei']
print(arr)