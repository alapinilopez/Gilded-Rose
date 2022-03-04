from os import name


from src.item import Item
from src.updateable import Updatable

class NormalItem(Item, Updatable):
    def __init__(self, name, sellIn, quality):
        super().__init__(self, name, sellIn, quality)


