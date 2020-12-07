class Bank1Account(object):
    tax = 1.0

    def __init__(self, number):
        self.number = number
        self.__total = 0

    def deposit(self, value):
        self.__total += value

    def withdraw(self, value):
        self.__total -= value
        # self.__total -= 1
        self.__total -= type(self).tax

    def getTotal(self):
        return self.__total


class Bank2Account(Bank1Account):
    tax = 2.0

    def __init__(self, number, cvv):
        super(Bank2Account, self).__init__(number)
        self.number = number
        self.cvv = cvv

    #def withdraw(self, value):
    #    self._Bank1Account__total -= value
    #    self._Bank1Account__total -= 2
