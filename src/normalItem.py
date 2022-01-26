from os import name


from src.item import Item
from src.updateable import Updatable

class NormalItem(Item, Updatable):
    def __init__(self, name, sellIn, quality):
        super().__init__(self, name, sellIn, quality)
    
    def setSellIn(self):
        self.sellIn = self.sellIn - 1
    
    def setQuality(self, value):
        if self.quality + value > 50:
            self.quality = 50
        elif self.quality + value >= 0:
            self.quality = self.quality + value
        else:
            self.quality = 0
        
    def updateQuality(self):
        if self.sellIn > 0:
            self.setQuality(-1)
        else:
            self.setQuality(-2)
        self.setSellIn()
