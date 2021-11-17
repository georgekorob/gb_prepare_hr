# 2. Написать программу, которая запрашивает у пользователя ввод числа. На введенное число она отвечает сообщением,
# целое оно или дробное. Если дробное — необходимо далее выполнить сравнение чисел до и после запятой.
# Если они совпадают, программа должна возвращать значение True, иначе False.


def check_number(number: str):
    from decimal import Decimal
    if number.isdigit():
        print(f'Число {number} - целое!')
    else:
        try:
            # Предложенный метод в чате вебинара math.modf возвращает неточное значение дробной части даже из Decimal
            number_dec = Decimal(number)
            num_int = int(number_dec)
            num_frac = number_dec % 1
            print(f'Число {number_dec} - дробное! Целая часть: {num_int}! Дробная часть: {num_frac}!')
            return num_int == int(str(num_frac)[2:])
        except Exception as e:
            print('Необходимо ввеcти число!', e)


# numbers = ['24', '532.52', '1.1']
# for n in numbers:
#     result = check_number(n)
#     if result is not None:
#         print(result)

input_number = input('Введите число: ')
result = check_number(input_number)
if result is not None:
    print(result)

# Число 24 - целое!
# Число 532.52 - дробное! Целая часть: 532! Дробная часть: 0.52!
# False
# Число 1.1 - дробное! Целая часть: 1! Дробная часть: 0.1!
# True
