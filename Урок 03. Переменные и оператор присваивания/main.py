a = 4
print(a)
print(a * 5)
print(a + a)
a = 54
print(a)
print(a + 5)
b = 10
print(a + b)
# print(c) # Получим ошибку - NameError: name 'c' is not defined, поскольку переменной c не существует!
c = 1
print(c)
c = 4
print(c)
age = 20
print(type(age))
money = 1.5
print(type(money))
# 1a = 10 # Нельзя создавать переменные с числа
# print(1a) # Получим ошибку - SyntaxError: invalid decimal literal
a1 = 10
print(a1)
# print(Age) # Получим ошибку - NameError: name 'Age' is not defined, т.к Python чувствителен к регистру!
# True = 3
# print(True) # Получим ошибку - SyntaxError: cannot assign to True, т.к нельзя использовать ключевые слова!
'''
Ключевые слова - false, class, finaly, is, return, None, continue, for, lambda, try, True, def, from, nonlocal, while
and, del, global, not, with, as, elif, if, or, yield, assert, else, import, pass, break, except, in, raise
'''
print(max(3, 4, 5))
max = 6
print(max)
# print(max(4, 53)) # Получим ошибку - TypeError: 'int' object is not callable, т.к объявили переменную max
my_money = 100 # snake_case
myMoney = 200 # cameCase
print(my_money, myMoney)
a = 4
a = 5.6
a = 'Строка'
print(a) # Динамическая типизация - переменная может принимать значения любых типов данных
b = 10
b = 2 * b
print(b)
b = 2 * b
print(b)
a = 5
c = b + 2 * a
print(c)
a = b = c = r = 1
print(a)
print(b)
print(c)
print(r)
a, b = 2, 7
print(a)
print(b)
print(a, b)
t = a
a = b
b = t
print(a, b)
a = a - 5
b = b + 5
print(a, b)