class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter
        self.radius = diameter / 2

    def calculate_circumference(self):
        return Circle.__pi * self.diameter

    def calculate_area(self):
        return Circle.__pi * self.radius * self.radius

    def calculate_area_of_sector(self, angle):
        return (angle / 360) * self.radius * self.radius * Circle.__pi


user_diameter = 10
user_angle = 5

circle = Circle(user_diameter)
print(circle.calculate_circumference())
print(circle.calculate_area())
print(circle.calculate_area_of_sector(user_angle))