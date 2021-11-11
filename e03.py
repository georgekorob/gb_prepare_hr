# 3. Разработать генератор случайных чисел. В функцию передавать начальное и конечное число генерации (нуль
# необходимо исключить). Заполнить этими данными список и словарь. Ключи словаря должны создаваться по шаблону:
# “elem_<номер_элемента>”. Вывести содержимое созданных списка и словаря.
from pprint import pprint

random_seed = 0


def generate_random_number(a, b):
    import time
    import hashlib
    from functools import reduce
    from operator import mul
    global random_seed
    result = 0
    while result == 0:
        time_now = time.time() + random_seed
        random_seed += 1
        hash_time = hashlib.md5(bytes(str(time_now), encoding='utf-8')).hexdigest()
        num_hashs = [int(ch) + 1 if ch.isdigit() else ord(ch) - 86 for ch in hash_time]
        result = reduce(mul, num_hashs[:16]) / reduce(mul, num_hashs[16:])
        if result == 1:
            break
        result = abs(result - int(result))
    return result * (b - a) + a


elem_dict = {}
elem_list = []
for i in range(10):
    random_number = generate_random_number(-10, 10)
    elem_dict[f'elem_{i}'] = random_number
    elem_list.append(random_number)

pprint(elem_list)
pprint(elem_dict)

# [-9.645250692869741,
#  -4.513031550068587,
#  -7.435937366040809,
#  -1.2167832167832149,
#  -5.245752875382505,
#  4.693877551020478,
#  8.971313393082099,
#  -3.3968253968259887,
#  -9.2996632996633,
#  -7.150598689060228]
# {'elem_0': -9.645250692869741,
#  'elem_1': -4.513031550068587,
#  'elem_2': -7.435937366040809,
#  'elem_3': -1.2167832167832149,
#  'elem_4': -5.245752875382505,
#  'elem_5': 4.693877551020478,
#  'elem_6': 8.971313393082099,
#  'elem_7': -3.3968253968259887,
#  'elem_8': -9.2996632996633,
#  'elem_9': -7.150598689060228}
