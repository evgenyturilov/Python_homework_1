# Задача 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

my_nums = [1.2, 3.4, 2.7, 4.3, 8.5]

excess_nums = [round(my_nums[i] - int(my_nums[i]), 5) for i in range(len(my_nums))]
print(round(max(excess_nums) - min(excess_nums), 5))