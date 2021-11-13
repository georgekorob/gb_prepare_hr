# 2. Инкапсулировать оба параметра (название и цену) товара родительского класса. Убедиться, что при сохранении
# текущей логики работы программы будет сгенерирована ошибка выполнения. Усовершенствовать родительский класс таким
# образом, чтобы получить доступ к защищенным переменным. Результат выполнения заданий 1 и 2 должен быть идентичным.

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


class ItemDiscountReport(ItemDiscount):
    """Дочерний класс"""

    def get_parent_data(self):
        return f'{self.name}: {self.price}'


item_parent = ItemDiscount()
item = ItemDiscountReport()
print(f'{item_parent.__doc__}: {hasattr(item_parent, "get_parent_data")}')
print(f'{item.__doc__}: {hasattr(item, "get_parent_data")}')
print(item.get_parent_data())

# После добавления защиты переменных (двойного подчеркивания). Вывод ошибки:
# AttributeError: 'ItemDiscountReport' object has no attribute '_ItemDiscountReport__name'

# После добавления getter-ов. Вывод как и в 1 задаче:
# Родительский класс: False
# Дочерний класс: True
# Table: 1000
