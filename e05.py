# 5. Усовершенствовать первую функцию из предыдущего примера. Необходимо во втором списке часть строковых значений
# заменить на значения типа example345 (строка+число). Далее — усовершенствовать вторую функцию из предыдущего
# примера (функцию извлечения данных). Дополнительно реализовать поиск определенных подстрок в файле по следующим
# условиям: вывод первого вхождения, вывод всех вхождений. Реализовать замену всех найденных подстрок на новое
# значение и вывод всех подстрок, состоящих из букв и цифр, например: example345.


def read_file(file):
    import re
    with open(file, 'r') as f:
        text = f.read()
        # Дополнительно реализовать поиск определенных подстрок в файле по следующим условиям:
        # вывод первого вхождения, вывод всех вхождений.
        pattern = r'ex[d-h] \d'
        all_inners = [f.start() for f in re.finditer(pattern, text)]
        print(f'Первое вхождение подстроки в файл: {all_inners[0]}')
        print(f'Остальные вхождения подстроки в файл: {all_inners[1:]}')
        # Реализовать замену всех найденных подстрок на новое значение
        print(text)
        text = re.sub(pattern, 'newString', text)
        print(text)
        # вывод всех подстрок, состоящих из букв и цифр, например: example345.
        for line in re.findall(r'[A-Za-z]+[0-9]+', text):
            print(line)


def write_file():
    import os
    file_name = 'file_for_e05.txt'
    if os.path.exists(file_name):
        print('Файл уже существует!')
        return
    try:
        with open(file_name, 'w') as f:
            text_info = (f'ex{chr(i)}' for i in range(100, 110))
            nums_info = (i for i in range(10))
            info = zip(text_info, nums_info)
            for ind, inf in enumerate(info):
                f.write(f'{inf[0]} {inf[1]}\n')
                if ind % 3 == 0:
                    f.write('example345\n')
        read_file(file_name)
    except Exception as e:
        print(e)
        os.remove(file_name)


write_file()

# Первое вхождение подстроки в файл: 0
# Остальные вхождения подстроки в файл: [17, 23, 29, 46]
# exd 0
# example345
# exe 1
# exf 2
# exg 3
# example345
# exh 4
# exi 5
# exj 6
# example345
# exk 7
# exl 8
# exm 9
# example345
#
# newString
# example345
# newString
# newString
# newString
# example345
# newString
# exi 5
# exj 6
# example345
# exk 7
# exl 8
# exm 9
# example345
#
# example345
# example345
# example345
# example345
