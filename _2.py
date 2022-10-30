#Задание 2
#Функция, возвращающая три списка
def divided_on(num_list):
    on_2 = [n for n in num_list
            if n%2 == 0]
    on_3 = [n for n in num_list
            if n%3 == 0]
    on_5 = [n for n in num_list
            if n%5 == 0]
    return on_2, on_3, on_5


#реализация функции
num_list = [2,3,4,5,6,22,33,44,55,66,7,9]
on_2, on_3, on_5 = divided_on(num_list)

print ('Делятся на 2:\n', on_2)
print ('Делятся на 3:\n', on_3)
print ('Делятся на 5:\n', on_5)
