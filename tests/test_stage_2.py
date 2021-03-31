import unittest

from farm import Farm
from crops import Crop

farmSize = 20

class TestStage2(unittest.TestCase):
  def setUp(self):
    self.farm = Farm(farmSize)

  def test_get_farm_size(self):
    self.assertEqual(self.farm.get_size(), farmSize)

  def test_add_small_crop(self):
    result = self.farm.add(Crop("badger", 1, 10))

    self.assertTrue(result)

  def test_cant_add_more_crops_than_size(self):
    result = self.farm.add(Crop("mice", 21, 10))

    self.assertFalse(result)

  def test_add_multiple_crops_up_to_size(self):
    self.farm.add(Crop("ferret", 10, 10))
    result = self.farm.add(Crop("weasel", 10, 10))

    self.assertTrue(result)

  def test_cant_add_multiple_over_size(self):
    self.farm.add(Crop("ferret", 10, 10))
    result = self.farm.add(Crop("weasel", 12, 10))

    self.assertFalse(result)

  def test_zero_value_with_no_crops(self):
    self.assertEqual(self.farm.get_total_sell_price(), 0)

  def test_can_get_total_value_of_added_crops(self):
    self.farm.add(Crop("mongoose", 4, 4))
    self.farm.add(Crop("meerkat", 10, 23))

    self.assertEqual(self.farm.get_total_sell_price(), 246)


if __name__ == "__main__":
  unittest.main()