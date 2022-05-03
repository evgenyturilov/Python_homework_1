# Задача 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

my_nums = [4, 6, 8, 3, 12, 5, 3, 7, 10]

def sum_of_odd_elements(lst):
    sum = 0
    for i in range(len(lst)):
        if i%2 != 0:
            sum += lst[i]
    return sum

print(sum_of_odd_elements(my_nums))

# Решение 2. С помощью встроенных функций Python

my_nums = [1, 2, 1, 2, 3, 1]

print(sum([my_nums[i] for i in range(len(my_nums)) if i%2 != 0 ]))