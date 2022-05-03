# Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

print('Введите десятичное число: ')
dec_num = temp_num = int(input())
bin_num = str()

while temp_num > 0:
    bin_num += str(temp_num%2)
    temp_num = temp_num//2

print(f'({dec_num} -> {bin_num[::-1]})')                # Переворачиваю результат bin_num