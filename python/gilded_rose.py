class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class NormalItemStrategy:
    def update(self, item):
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = max(0, item.quality - 2)
        else:
            item.quality = max(0, item.quality - 1)


class AgedBrieStrategy:
    def update(self, item):
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = min(50, item.quality + 2)
        else:
            item.quality = min(50, item.quality + 1)


class SulfurasStrategy:
    def update(self, item):
        pass  # 永不改变


class BackstagePassStrategy:
    def update(self, item):
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = 0
        elif item.sell_in < 5:
            item.quality = min(50, item.quality + 3)
        elif item.sell_in < 10:
            item.quality = min(50, item.quality + 2)
        else:
            item.quality = min(50, item.quality + 1)


class ConjuredStrategy:
    def update(self, item):
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = max(0, item.quality - 4)
        else:
            item.quality = max(0, item.quality - 2)


class GildedRose(object):

    STRATEGIES = {
        "Aged Brie": AgedBrieStrategy(),
        "Sulfuras, Hand of Ragnaros": SulfurasStrategy(),
        "Backstage passes to a TAFKAL80ETC concert": BackstagePassStrategy(),
        "Conjured Mana Cake": ConjuredStrategy(),
    }

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            strategy = self.STRATEGIES.get(item.name, NormalItemStrategy())
            strategy.update(item)