class ElectricCar:

    def __init__(self, max_range):
        self.__initial_max_range = max_range
        self.__max_range = max_range

    def range (self):
        return self.__max_range

    def drive(self, range_to_go):
        if self.__max_range>=range_to_go:
            self.__max_range= self.__max_range-range_to_go
            range_driven = range_to_go
        else:
            range_driven = self.__max_range
            self.__max_range = 0
        return range_driven

    def charge (self):
        self.__max_range = self.__initial_max_range
        return self.__max_range



