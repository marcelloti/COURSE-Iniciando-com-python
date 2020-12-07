class Car:
    someStaticPublicVar = 'Abc'

    def __init__(self, name, make, year):
        self.name = name
        self.make = make
        self.year = year

    def drive(self):
        print(self.name + " started")

    @staticmethod
    def hello():
        print("Hello from car")

    @classmethod
    def show(cls):
        print(cls.someStaticPublicVar)
