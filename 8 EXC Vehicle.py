class Vehicle:
    def __init__(self, type: str, model: str, price: int):
        self.type = type
        self.model = model
        self.price = price
        self.owner = None

    def buy(self, money: int, owner: str):
        if money >= self.price and self.owner is None:
            self.owner = owner
            return f'Successfully bought a {self.type}. Change: {money - self.price:.2f}'
        elif money < self.price:
            return f'Sorry, not enough money'
        elif self.owner:
            return 'Car already sold'

    def sell(self):
        if self.owner:
            self.owner = None
        else:
            return 'Vehicle has no owner'

    def __repr__(self):
        if self.owner:
            return f'{self.model} {self.type} is owned by: {self.owner}'
        else:
            return f'{self.model} {self.type} is on sale: {self.price}'


car1 = Vehicle('combi', 'Corrola', 2500)
car2 = Vehicle('truck', 'Volvo', 7000)
car3 = ['car', 'BMW', 15000]
car3 = Vehicle(car3[0], car3[1], car3[2])
print(car1)
print(car3)
vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
print(vehicle.buy(15000, "Peter"))
print(vehicle.buy(35000, "George"))
print(vehicle)
vehicle.sell()
print(vehicle)
