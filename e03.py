# 3. Создать два списка с различным количеством элементов. В первом должны быть записаны ключи, во втором — значения.
# Необходимо написать функцию, создающую из данных ключей и значений словарь. Если ключу не хватает значения,
# в словаре для него должно сохраняться значение None. Значения, которым не хватило ключей, необходимо отбросить.
from itertools import zip_longest

first_list = [1, 2, 3, 4]
second_list = [1, 2, 3]


def merge_to_dict(first, second):
    if len(first) > len(second):
        result = {f: s for f, s in zip_longest(first, second)}
    else:
        result = {f: s for f, s in zip(first, second)}
    print(result)


merge_to_dict(first_list, second_list)
second_list = [1, 2, 3, 4, 5]
merge_to_dict(first_list, second_list)

# {1: 1, 2: 2, 3: 3, 4: None}
# {1: 1, 2: 2, 3: 3, 4: 4}
