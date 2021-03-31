# -*-coding:utf-8-*-


class Crop:

    def __init__(self, name: str = 'crop', size: int = 0, sell_price: int = 1):
        """Defines a crop type that holds information about a crop type and amount
        :param name: name of the crop
        :param size: size of the crop
        :param sell_price: sell price of the crop
        """
        self.name = name
        self.size = size
        self.sell_price = sell_price

    def get_name(self) -> str:
        """Get name of the crop
        """
        return self.name

    def get_size(self) -> int:
        """Get size of the crop
        """
        return self.size

    def get_price_per_unit(self) -> int:
        """Get price per unit
        """
        return self.sell_price

    def total_sell_price(self) -> int:
        """Get total price of the crop
        """
        return self.get_price_per_unit()*self.get_size()
