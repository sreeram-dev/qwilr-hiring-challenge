# -*-coding:utf-8 -*-

import unittest

from qwilr.farm import Farm
from qwilr.crops import Crop

FARM_SIZE = 20

class TestStage3(unittest.TestCase):

    def test_single_fields(self):
        """
        """
        farm = Farm(20, [('grass', 10)])
        crops = [Crop('Cow', 4)]
        for crop in crops:
            result = farm.add(crop)
            self.assertTrue(result)

    def test_add_crop_fail_field_doesnot_exist(self):
        farm = Farm(20, [('dirt', 10)])
        crop = Crop('cow', 4)
        result = farm.add(crop)
        self.assertFalse(result)

    def test_multiple_fields(self):
        farm = Farm(20, [('dirt', 10), ('grass', 10)])
        crops = [Crop('cow', 5), Crop('carrot', 10)]
        for crop in crops:
            result = farm.add(crop)
            self.assertTrue(result)

    def test_multiple_crops_single_field_doesnot_exist(self):
        farm = Farm(20, [('dirt', 10)])
        crops = [Crop('cow', 5), Crop('carrot', 10)]
        # add cow should not succeed
        result = farm.add(crops[0])
        self.assertFalse(result)
        # add carrot should succeed
        result = farm.add(crops[1])
        self.assertTrue(result)

    def test_add_crop_fail_nospace(self):
        farm = Farm(20, [('dirt', 10)])
        crop = Crop('carrot', 20)
        # add cow should not succeed
        result = farm.add(crop)
        self.assertFalse(result)

    def test_add_crop_get_size(self):
        farm = Farm(20, [('dirt', 10), ('grass', 10)])
        crops = [Crop('cow', 5), Crop('carrot', 10)]
        for crop in crops:
            result = farm.add(crop)

        self.assertEqual(15, farm.get_size())
        self.assertEqual(10, farm.get_occupied_size_for_field('dirt'))
        self.assertEqual(5, farm.get_occupied_size_for_field('grass'))
