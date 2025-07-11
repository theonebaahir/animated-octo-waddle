class computer:
    def __init__(self):
        self.__maxprice = 900
    def sell(self):
        print("selling price {}". format(self.__maxprice))
    def setblah(self, price):
        self.__maxprice = price
c = computer()
c.sell()
c.__maxprice = 1000
c.sell()

c.setblah(1000)
c.sell()