import unittest

from qwilr.farm import Farm
from qwilr.crops import Crop


class TestStage1(unittest.TestCase):

    def setUp(self):
        self.farm = Farm()

    def test_add_crop(self):
        result = self.farm.add(Crop("pizza", 1))
        self.assertTrue(result)

    def test_add_multiple_crops(self):
        test_crops = [
            Crop("oranges", 3),
            Crop("apples", 2),
            Crop("watermelons", 30)
        ]

        for testCrop in test_crops:
            result = self.farm.add(testCrop)
            self.assertTrue(result)

    def test_get_empty_counts(self):
        self.assertEqual(self.farm.get_counts(), [])

    def test_get_single_crops_counts(self):
        self.farm.add(Crop("feta", 23))

        self.assertEqual(self.farm.get_counts(), [{
            "cropName": "feta",
            "amount": 23
        }])

    def test_get_multiple_crops_counts(self):
        self.farm.add(Crop("oysters", 12))
        self.farm.add(Crop("muscles", 11))

        self.assertEqual(self.farm.get_counts(), [
            {
                "cropName": "oysters",
                "amount": 12
            },
            {
                "cropName": "muscles",
                "amount": 11
            }])

    def test_get_multiple_same_crops_counts(self):
        self.farm.add(Crop("hot dogs", 5))
        self.farm.add(Crop("hot dogs", 10))

        self.assertEqual(self.farm.get_counts(), [{
            "cropName": "hot dogs",
            "amount": 15
        }])

    def test_get_total_crops(self):
        self.farm.add(Crop("poppy", 12))
        self.farm.add(Crop("daisy", 32))

        self.assertEqual(self.farm.get_total_count(), 44)


if __name__ == "__main__":
    unittest.main()
