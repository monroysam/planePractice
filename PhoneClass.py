
class Phone:

    def __init__(self, manu, modl, p):
        self.__manufact = manu
        self.__model = modl
        self.__retail_price = p

    def set_manufact(self, m):
        self.__manufact = m

    def set_model(self, m):
        self.__model = m

    def set_price(self, p):
        self.__retail_price = p


    def get_manufact(self):
        return self.__manufact
    
    def get_model(self):
        return self.__model
    
    def get_price(self):
        return self.__retail_price
    
