from mimetypes import init
from src.normalItem import NormalItem

class Sulfuras(NormalItem):
    def __init__(self, name, sellIn, quality):
        super().__init__(name, sellIn, quality)
    
    def setQuality(self, value):
        return super().setQuality(value)
    
    def setSellIn(self):
        return super().setSellIn()
    
    def updateQuality(self):
        self.quality == 80
