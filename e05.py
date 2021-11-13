# 5. Проверить на практике возможности полиморфизма. Необходимо разделить дочерний класс ItemDiscountReport на два
# класса. Инициализировать классы необязательно. Внутри каждого поместить функцию get_info, которая в первом классе
# будет отвечать за вывод названия товара, а вторая — его цены. Далее реализовать выполнение каждой из функции тремя
# способами.

class ItemDiscount:
    """Родительский класс"""
    __name = 'Table'
    __price = 1000

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    def get_info(self):
        raise NotImplementedError


class ItemDiscountReportOne(ItemDiscount):
    """Дочерний класс 1"""

    @property
    def get_info(self):
        return self.name


class ItemDiscountReportTwo(ItemDiscount):
    """Дочерний класс 2"""

    @property
    def get_info(self):
        return self.price


item1 = ItemDiscountReportOne()
item2 = ItemDiscountReportTwo()
print(getattr(item1, 'get_info'))
print(getattr(item2, 'get_info'))
print(item1.get_info)
print(item2.get_info)

# Вывод:
# Table
# 1000
# Table
# 1000

# Непонятно, какие 3 способа использовать для выполнения каждой из функций.
