# Даны 2 неупорядоченных набора целых чисел (может быть с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются
# в обоих наборах. Пользователь вводит 2 числа т - кол-во элементов первого 
# множества. ь - кол-во элементов второго множества. Затем пользователь вводи 
# сами множества.
import random
lenght_list_1 = int(input('Введите кол-во элементов первого списка: '))
lenght_list_2 = int(input('Введите кол-во элементов второго списка: '))
list_1 = [random.randint(10, 100) for _ in range(lenght_list_1)]
print(f"Первый набор чисел: \n{list_1}")
list_2 = [random.randint(10, 100) for _ in range(lenght_list_2)]
print(f"Второй набор чисел: \n{list_2}")
sorted_list_1 = sorted(list_1)
print(f"Список 1: сортировка значений по возрастанию: \n{sorted_list_1}")
sorted_list_2 = sorted(list_2)
print(f"Список 2: сортировка значений по возрастанию: \n{sorted_list_2}")
set_from_list_1 = set(sorted_list_1)
print(f"Множество 1: Удалены все повторяющиеся значения: \n{set_from_list_1}")
set_from_list_2 = set(sorted_list_2)
print(f"Множество 2: Удалены все повторяющиеся значения: \n{set_from_list_2}")
our_new_list = set_from_list_1.union(set_from_list_2)
print(f"Все уникальные значения в порядке возрастания, которые встречаются в этих наборах чисел: \n{our_new_list}")