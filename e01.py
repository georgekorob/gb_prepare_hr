# 1. Проверить механизм наследования в Python. Для этого создать два класса. Первый — родительский (ItemDiscount),
# должен содержать статическую информацию о товаре: название и цену. Второй — дочерний (ItemDiscountReport),
# должен содержать функцию (get_parent_data), отвечающую за отображение информации о товаре в одной строке. Проверить
# работу программы, создав экземпляр (объект) родительского класса.

class ItemDiscount:
    """Родительский класс"""
    name = 'Table'
    price = 1000


class ItemDiscountReport(ItemDiscount):
    """Дочерний класс"""
    def get_parent_data(self):
        return f'{self.name}: {self.price}'


item_parent = ItemDiscount()
item = ItemDiscountReport()
print(f'{item_parent.__doc__}: {hasattr(item_parent, "get_parent_data")}')
print(f'{item.__doc__}: {hasattr(item, "get_parent_data")}')
print(item.get_parent_data())

# Вывод:
# Родительский класс: False
# Дочерний класс: True
# Table: 1000

# Из условия задачи непонятно, зачем нужно создавать экземпляр родительского класса.
