#Задание 3 
#Функция, принимающая на вход int, и возвращающая число, обратное этому int
def inver(num: int):
    if num>=0:  
        num_ = str(num)       
        num_ = num_[::-1]     #разворот строки
    else:       #если число отрицательное      
        num_ = [d for d in str(num)]   #инициализация и заполнение списка
        num_ = num_[::-1]             #разворот списка
        num_.insert(0, num_.pop(-1))  #перенос минуса в начало списка
    return int(''.join(num_))  #возврат int 

#реализация работы функции
print (inver(123))
print (inver(-123))
print (inver(120))
print (inver(0))
