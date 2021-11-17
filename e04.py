# 4. Написать программу, в которой реализовать две функции. В первой должен создаваться простой текстовый файл.
# Если файл с таким именем уже существует, выводим соответствующее сообщение. Необходимо открыть файл и подготовить
# два списка: с текстовой и числовой информацией. Для создания списков использовать генераторы.
# Применить к спискам функцию zip(). Результат выполнения этой функции должен должен быть обработан и записан
# в файл таким образом, чтобы каждая строка файла содержала текстовое и числовое значение. Вызвать вторую функцию.
# В нее должна передаваться ссылка на созданный файл. Во второй функции необходимо реализовать открытие файла и
# простой построчный вывод содержимого. Вся программа должна запускаться по вызову первой функции.


def read_file(file):
    with open(file, 'r') as f:
        while 1:
            line = f.readline().strip()
            if not line:
                return
            print(line)


def write_file():
    import os
    file_name = 'file_for_e04.txt'
    if os.path.exists(file_name):
        print('Файл уже существует!')
        return
    try:
        with open(file_name, 'w') as f:
            text_info = (f'ex{chr(i)}' for i in range(100, 110))
            nums_info = (i for i in range(10))
            info = zip(text_info, nums_info)
            for i in info:
                f.write(f'{i[0]} {i[1]}\n')
        read_file(file_name)
    except Exception as e:
        print(e)
        os.remove(file_name)


write_file()

# exd 0
# exe 1
# exf 2
# exg 3
# exh 4
# exi 5
# exj 6
# exk 7
# exl 8
# exm 9
