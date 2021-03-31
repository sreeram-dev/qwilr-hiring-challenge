# -*-coding:utf-8-*-

from collections import defaultdict
from typing import List, Tuple

from qwilr.crops import Crop


def get_field_type_for_crop(crop_name: str) -> str:
    """

    """
    crop_name = crop_name.lower()
    if crop_name == 'carrot':
        return 'dirt'

    if crop_name == 'cow':
        return 'grass'


class Farm:
    """Class to denote a farm in the farm management app
    # [1, 2, 3]
    # [('grass', 3), ('dirt', 4)]
    """

    def __init__(self, max_size: int = 100, fields: List[Tuple[str, int]] = []):
        """Create a farm
        """
        self.fields = defaultdict(int)
        # keeping a dictionary for fast lookups
        for field, field_size in fields:
            self.fields[field.lower()] += field_size

        self.max_size = max_size
        self.crops = []

    def add(self, crop: Crop) -> bool:
        """Add a crop onto the farm
        :param crop: Crop object
        :return: return if the crop is true
        """
        try:
            self.__validate_crop_addition(crop)
        except ValueError as e:
            print(e)
            return False
        except KeyError:
            return False

        self.crops.append(crop)

        return True

    def __validate_crop_addition(self, crop: Crop):
        """Validates if the crop is valid and total size is
        not exceeded.
        """

        ###
        ## Two Scenarios
        # - field is not present
        # - field is present, but there is no space available
        ###

        # field of the current crop we want to add
        field_type = get_field_type_for_crop(crop.get_name())
        if field_type not in self.fields:
            raise KeyError(f"Crop cannot be added if field is not present")

        # this is size of the field present in the farm
        # cannot add of crop of size that exceeds the field size
        max_allowed_size = self.fields[field_type]

        # size of the crops with the matching field_type
        current_size = 0
        for old_crop in self.crops:
            old_crop_field_type = get_field_type_for_crop(old_crop.get_name())
            if old_crop_field_type == field_type:
                current_size += old_crop.get_size()

        if current_size + crop.get_size() > max_allowed_size:
            raise ValueError(f"Cannot add value of size: {crop.get_size()} field is full")

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

    def get_occupied_size_for_field(self, field: str) -> int:
        """Grass field of size (grass: 10, total_acres: 300)
        ## (3, 3, 4) -> disjoint plots
        ## (3, 2) -> 3 cows in plot and 2 cows in another => (0, 1, 4) - 1 size of a plot and complete plot
        ## get_total_size_for_field -> get all the current occupied fields
        """
        if field not in self.fields:
            raise KeyError("Field does not exist")

        occupied_size = 0
        for crop in self.crops:
            crop_field = get_field_type_for_crop(crop.get_name())
            if crop_field == field:
                occupied_size += crop.get_size()

        return occupied_size

    def get_size(self) -> int:
        """Get the total size of the farm
        """
        total_size = 0
        for crop in self.crops:
            total_size += crop.get_size()

        return total_size

    def get_total_sell_price(self) -> int:
        """Get the total price of the farm
        """
        total = 0
        for crop in self.crops:
            total += crop.total_sell_price()

        return total
###
###
# Farm of type cannot accept another type
# Grass farm => [('', ), '', ''] ('type', 10)
# Farm(fields,
# a crop cannot be added if the farm size is full
# a crop cannot be added if the farm type does not exist
# Whenever, we are not able to add, we have to return false
# it has to be a keyword

## get_size => sum of sizes of all feilds
