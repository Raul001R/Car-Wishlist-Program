class Car:
    def __init__(self, year, make, model, price, mileage, link):
        self.year = year
        self.make = make
        self.model = model
        self.price = price
        self.mileage = mileage
        self.link = link

    def __str__(self):
        return f"{self.year} {self.make} {self.model} ${self.price} {self.mileage} miles {self.link}"
