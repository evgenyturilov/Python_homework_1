# Задача 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def list_of_negafibonacci(num):
    list_of_negafibonacci = list()
    for i in range(-num, num + 1):
        if i < 0:
            list_of_negafibonacci.append(-fibonacci(abs(i)))
        elif i == 0:
            list_of_negafibonacci.append(0)
        else:
            list_of_negafibonacci.append(fibonacci(i))
    return list_of_negafibonacci


print("Введите целое число: ")
num = int(input())
print(list_of_negafibonacci(num))
