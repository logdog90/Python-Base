# a = input() # Функция вернёт строку
# print(type(a))
# # print(a + 2) # Получим ошибку - TypeError: can only concatenate str (not "int") to str
# # Нельзя складывать строку с числом
# # print(a * 2) # Строка увеличится в 2 раза, получаем скокатенированное число, например 123123
# b = int(input()) # Функция int перевдит строку в число
# print(type(b))
# print(int('4.5')) # Получим ошибку - ValueError: invalid literal for int()
# В функции int нельзя пребразовывать строки и дробные числа
# print(int('Строка')) # Получим ошибку - ValueError: invalid literal for int()
# В функции int нельзя пребразовывать стоки
# print(float(4)) # Преобразовываем целое число 4 в дробное 4.0 
# print(float('5')) # Преобразовываем строку '5' в дробное число 4.0
# # print(float('Строка') # Преобразовывать строку 'Строка' в дробное число нельзя, получим ошибку
# # ValueError: could not convert string to float: 'Строка'
# c = float(input())
# e = int(input()) # Преобразовываем строку в число
# print(e + 2) # Складываем переменную
# print(e * 2) # Умножаем переменную
# d = int(input()) # Если передадим число, например 10строка, то получим ошибку ValueError: invalid literal for int()

# Программа для поиска периметра трехугольника
a = float(input('Введите сторону a: '))
b = float(input('Введите сторону b: '))
c = float(input('Введите сторону c: '))
p = a + b + c

# В строку
a, b, c = map(int, input().split())
p = a + b + c
print(p)

# Задача
a = int(input('Введите значение: '))
print(a * a) # Число в квадрате