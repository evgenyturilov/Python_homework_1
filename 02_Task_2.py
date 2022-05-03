# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

my_nums = [1, 2, 3, 4, 5, 6, 7]

def multiplication_of_pair_elements(origin_list):
    result_list = list()
    lenght = round(len(origin_list)/2)              # делаю округление для того, чтобы в случае нечетного количества элементов в списке,
                                                    # "центральный" элемент перемножался сам на себя, как в примере см. README.md
    for i in range(lenght):
        j = -i - 1
        mult = origin_list[i]*origin_list[j]
        result_list.append(mult)
    return result_list

print(multiplication_of_pair_elements(my_nums))