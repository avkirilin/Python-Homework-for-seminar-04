# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке,
# причем кусты высажены только по окружности.Таким образом, у каждого куста есть ровно
# два соседних. Всего на грядке растет N кустов. Эти кусты обладают разной урожайностью,
# поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло
# ai ягод. В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий
# модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с
# этого куста и с двух соседних с ним. Напишите программу для нахождения максимального
# числа ягод, которое может собрать за один заход собирающий модуль, находясь перед 
# некоторым кустом заданной во входном файле грядки.
import random
count_bashes = random.randrange(9, 99, 3)
print(f"Кол-во кустов, растущих на грядке: {count_bashes}")
bush_yield_list = [random.randint(1, 10) for _ in range(count_bashes)]
print(f"Список урожайности кустов на грядке: \n{bush_yield_list}")
max_num_of_berries = 0
for item in range(count_bashes):
    count_of_berries = 0
    if item == 0:
        count_of_berries = bush_yield_list[0] + bush_yield_list[1] + bush_yield_list[-1]
        if max_num_of_berries < count_of_berries:
            max_num_of_berries = count_of_berries
    elif item == count_bashes - 1:
        count_of_berries = bush_yield_list[-1] + bush_yield_list[0] + bush_yield_list[-2]
        if max_num_of_berries < count_of_berries:
            max_num_of_berries = count_of_berries
    else:
        count_of_berries = bush_yield_list[item] + bush_yield_list[item + 1] + bush_yield_list[item - 1]
        if max_num_of_berries < count_of_berries:
            max_num_of_berries = count_of_berries
print(f'Максимальное кол-во ягод, которое может собрать собирающий модуль за один раз: {max_num_of_berries}')
