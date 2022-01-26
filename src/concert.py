from src.normalItem import NormalItem

class Concert(NormalItem):
    def __init__(self, name, sellIn, quality):
        super().__init__(name, sellIn, quality)
    
    def setQuality(self, value):
        return super().setQuality(value)
    
    def setSellIn(self):
        return super().setSellIn()
    
    def updateQuality(self):
        if self.sellIn > 10:
            self.setQuality(1)
        elif self.sellIn <= 10:
            self.setQuality(2)
        elif self.sellIn <= 5:
            self.setQuality(3)
        else: 0
        self.setSellIn()
        