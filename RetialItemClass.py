class Item:

    def __init__(self, d, i, p):
        self.__description = d
        self.__inventory = i
        self.__price = p

    def __str__(self):
        return (f"DESCRIPTION: {self.__description:20}"
    f"  UNITS IN INVENTORY: {self.__inventory:<5}"
    f"  PRICE: ${self.__price}")