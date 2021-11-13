# 3. Реализовать возможность переустановки значения цены товара. Необходимо, чтобы и родительский, и дочерний классы
# получили новое значение цены. Следует проверить это, вызвав соответствующий метод родительского класса и функцию
# дочернего (функция, отвечающая за отображение информации о товаре в одной строке).

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

    def get_parent_data(self):
        return f'{self.name}: {self.price}'


item_parent = ItemDiscount()
item = ItemDiscountReport()
item.set_price(1400)
print(item_parent.name, item_parent.price)
print(item.get_parent_data())

# Вывод:
# Table 1400
# Table: 1400
