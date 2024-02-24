class Car:
    def __init__(self, make, model, year, price):
        self.make = make
        self.model = model
        self.year = year
        self.price = price

    def get_info(self):
        return f"{self.year} {self.make} {self.model} - ${self.price}"
