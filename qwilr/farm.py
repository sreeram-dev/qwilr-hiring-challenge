# -*-coding:utf-8-*-

from collections import defaultdict

from qwilr.crops import Crop


class Farm:
    """Class to denote a farm in the farm management app
    """

    def __init__(self, max_size: int = 100):
        self.crops = []
        self.max_size = max_size

    def add(self, crop: Crop) -> bool:
        """Add a crop onto the farm
        :param crop: Crop object
        :return: return if the crop is true
        """
        try:
            self.__validate_crop_addition(crop)
        except ValueError:
            return False

        self.crops.append(crop)

        return True

    def __validate_crop_addition(self, crop: Crop):
        """Validates if the crop is valid and total size is
        not exceeded.
        """
        present_size = 0
        for old_crop in self.crops:
            present_size += old_crop.get_size()

        if present_size + crop.get_size() > self.max_size:
            raise ValueError(f"Cannot add value of size: {crop.get_size()}")

    def get_counts(self) -> int:
        """Get the counts per crop in the farm
        :return: number of crops in the farm
        """

        # Each crop planted can be unique and on disjoint plots,
        # so not coupling all the crops
        # in the result, counts against name are aggregated
        counts = defaultdict(int)
        for crop in self.crops:
            counts[crop.get_name()] += crop.get_size()
        tuples = [{'cropName': crop_name, 'amount': total_size}
                  for crop_name, total_size in counts.items()]
        return tuples

    def get_total_count(self) -> int:
        """Get the total count of crops in the farm
        :return: int
        """
        total = 0
        for crop in self.crops:
            total += crop.get_size()
        return total

    def get_size(self) -> int:
        """Get the total size of the farm
        """
        return self.max_size

    def get_total_sell_price(self) -> int:
        """Get the total price of the farm
        """
        total = 0
        for crop in self.crops:
            total += crop.total_sell_price()

        return total
