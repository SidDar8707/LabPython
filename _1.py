#Задание 1
#Функция для проверки палиндромов
def palindrome (number: int): 
    number = str(number) #преобразование int в строку
    return number == number[::-1]#вернет True или False

#реализация работы функции
print(palindrome(121))
print(palindrome(123)) 
print(palindrome(12345))
print(palindrome(44144))
