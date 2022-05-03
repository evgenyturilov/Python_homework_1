# Задача 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

import Fibonnaci_rec as f_rec         # Импорт функции расчета чисел Фибоначчи рекурсивным методом из файла Fibonacci_rec.py

def list_of_negafibonacci(num):
    list_of_negafibonacci = list()
    for i in range(-num, num + 1):
        if i < 0:
            list_of_negafibonacci.append(-f_rec.fibonacci_rec(abs(i)))
        elif i == 0:
            list_of_negafibonacci.append(0)
        else:
            list_of_negafibonacci.append(f_rec.fibonacci_rec(i))
    return list_of_negafibonacci


print("Введите целое число: ")
num = int(input())
print(list_of_negafibonacci(num))
