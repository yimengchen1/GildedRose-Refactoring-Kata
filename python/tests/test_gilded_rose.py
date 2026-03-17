import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):

    # Test of ordinary items
    def test_normal_item_quality_decreases_by_one(self):
        items = [Item("Normal Item", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(19, items[0].quality)

    def test_normal_item_sellin_decreases_by_one(self):
        items = [Item("Normal Item", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].sell_in)

    def test_normal_item_quality_degrades_twice_after_expiry(self):
        items = [Item("Normal Item", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(18, items[0].quality)

    def test_normal_item_quality_never_negative(self):
        items = [Item("Normal Item", 10, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    # Test of Aged Brie 
    def test_aged_brie_quality_increases(self):
        items = [Item("Aged Brie", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(21, items[0].quality)

    def test_aged_brie_quality_increases_twice_after_expiry(self):
        items = [Item("Aged Brie", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(22, items[0].quality)

    def test_aged_brie_quality_never_exceeds_50(self):
        items = [Item("Aged Brie", 10, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    # Test of Sulfuras 
    def test_sulfuras_quality_never_changes(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(80, items[0].quality)

    def test_sulfuras_sellin_never_changes(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(10, items[0].sell_in)

    # Test of Backstage passes
    def test_backstage_pass_quality_increases_by_one_normal(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(21, items[0].quality)

    def test_backstage_pass_quality_increases_by_two_within_10_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(22, items[0].quality)

    def test_backstage_pass_quality_increases_by_three_within_5_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(23, items[0].quality)

    def test_backstage_pass_quality_drops_to_zero_after_concert(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_backstage_pass_quality_never_exceeds_50(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    # Test of Conjured
    def test_conjured_quality_degrades_twice_as_fast(self):
        items = [Item("Conjured Mana Cake", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(18, items[0].quality)

    def test_conjured_quality_degrades_four_times_after_expiry(self):
        items = [Item("Conjured Mana Cake", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(16, items[0].quality)

    def test_conjured_quality_never_negative(self):
        items = [Item("Conjured Mana Cake", 10, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)


if __name__ == '__main__':
    unittest.main()
