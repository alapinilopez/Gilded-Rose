class GildedRose(object):
    def __init__(self, stock):
        self.stock = stock

    def updateQuality(self):
        for item in self.stock:
                item.updateQuality()