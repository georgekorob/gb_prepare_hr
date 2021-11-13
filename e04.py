# 4. Реализовать расчет цены товара со скидкой. Величина скидки должна передаваться в качестве аргумента в дочерний
# класс. Выполнить перегрузку методов конструктора дочернего класса (метод __init__, в который должна передаваться
# переменная — скидка), и перегрузку метода __str__ дочернего класса. В этом методе должна пересчитываться цена и
# возвращаться результат — цена товара со скидкой. Чтобы все работало корректно, не забудьте инициализировать
# дочерний и родительский классы (вторая и третья строка после объявления дочернего класса).

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

    @staticmethod
    def set_price(value):
        ItemDiscount.__price = value


class ItemDiscountReport(ItemDiscount):
    """Дочерний класс"""

    def __init__(self, discount):
        self.discount = discount

    def __str__(self):
        return f'{self.price * (1 - self.discount / 100)}'

    def get_parent_data(self):
        return f'{self.name}: {self.price}'


item_parent = ItemDiscount()
item = ItemDiscountReport(10)
item.set_price(1400)
print(item_parent.price)
print(item)

# Вывод:
# 1400
# 1260.0

# Из условия задачи непонятно, почему нужно создавать перегрузку именно метода __str__. И непонятно, почему,
# "чтобы все работало корректно, не забудьте инициализировать дочерний и родительский классы", ведь для проверки
# достаточно только дочернего класса или я чего-то не понимаю?
# Ещё непонятно, что это за (вторая и третья строка после объявления дочернего класса).
