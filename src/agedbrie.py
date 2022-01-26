from src.normalItem import NormalItem


class AgedBrie(NormalItem):
    def __init__(self, name, sellIn, quality):
        super().__init__(name, sellIn, quality)
    
    def setQuality(self, value):
        return super().setQuality(value)
    
    def setSellIn(self):
        return super().setSellIn()
    
    def updateQuality(self):
        if self.sellIn > 0:
            self.setQuality(1)
        else:
            self.setQuality(2)