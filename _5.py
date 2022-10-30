#Задание №5. Функция, проверяющая, простое число или нет (диапазон от 1 до 100000).
def ProverkaProstNumb(num):
    if num<1 or num>100000: #принадлежит число диапазону [1;100000] или нет
        return
    k = 0
    for i in range(2, num // 2+1):
        if (num % i == 0):
            k = k+1
    return k <= 0

#реализация работы функции
print (ProverkaProstNumb(5))
print (ProverkaProstNumb(23))
print (ProverkaProstNumb(110))
