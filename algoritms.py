Найти простое число
# import math
# def is_prime(a):
#     if a == 2:
#         return True
#     if a % 2 == 0:
#         return False
#     for i in range(3, int(math.sqrt(a)) + 1, 2):
#         if a % i == 0:
#             return False
#     return True
#
# number = int(input('Введите число>>>'))
# if is_prime(number):
#     print('простое')
# else:
#     print('не простое')

# Задача о сортировке массива

# a = [123, 4, 23, 56, 78, 456]
# list = []
# while a:
#     minim = a[0]
#     for x in a:
#         if x < minim:
#             minim = x
#     list.append(minim)
#     a.remove(minim)
#
# print(list)

# Задача о поиске наибольшего элемента в массиве

# a = [123, 4, 23, 56, 78, 456]
# list = []
# while a:
#     minim = a[0]
#     for x in a:
#         if x < minim:
#             minim = x
#     list.append(minim)
#     a.remove(minim)
# num = list[-1]
#
# print(num)

#Задача о вычислении числа Фибоначчи
# x = int(input())
# a, b = 1, 1
#
# for i in range(1, x + 1):
#     print(i, ' >>> ', a)
#     a, b = b, a + b