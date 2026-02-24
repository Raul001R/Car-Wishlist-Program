from car import Car
import csv



class CarWishlist:
    def __init__(self):
        self.wishlist = []

    def add_car(self):
         year = input("what is the year?")
         make = input("what is the make?")
         model = input("what is the model?")
         price = input("what is the price?")
         mileage = input("what is the mileage?")
         link = input("what is the link?")
         my_car = Car(year,make,model,price,mileage,link)
         self.wishlist.append(my_car)

    def load(self):
        try:
            with open("CarWishlist.csv","r") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    my_car=Car(row["year"],row["make"],row["model"],row["price"],row["mileage"],row["link"])
                    self.wishlist.append(my_car)
        except FileNotFoundError:
            pass

    def remove_car(self):
        self.view_wishlist()
        choice = int(input("Which vehicle would you like to remove? pick a number"))
        self.wishlist.pop(choice)

    def save(self):
        with open("CarWishlist.csv", "w", newline="") as f:
         writer = csv.DictWriter(f, fieldnames=["year", "make", "model", "price", "mileage", "link"])
         writer.writeheader()
         for car in self.wishlist:
            writer.writerow({"year": car.year, "make": car.make, "model": car.model, "price": car.price,
                            "mileage": car.mileage, "link": car.link})

    def view_wishlist(self):
        for i, v in enumerate(self.wishlist):
            print(i,v)
            print("\n\n")

