class Car:
    def __init__(self, make, model, year, miles, price):
        self.make = make
        self.model = model
        self.year = year
        self.miles = miles
        self.price = price

    def __str__(self):
        return f"{self.year} {self.make} {self.model}:\n Mileage: {self.miles}\n Sticker Price: ${self.price}"


cars = []
cars.append(Car('Ford', 'Mustang', 2013, 25000, 37999))
cars.append(Car('Nissan', 'Xterra', 2004, 89500, 7500))
cars.append(Car('Nissan', 'Maxima', 2012, 25000, 15750))

for car in cars:
    print(car)
