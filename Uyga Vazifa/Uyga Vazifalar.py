# 1 - Masala

# class Car:
#     def __init__(self, model, price, year, color, engine):
#         self.model = model
#         self.price = price
#         self.year = year
#         self.color = color
#         self.engine = engine
#
#     def display_info(self):
#         print(f"Model: {self.model}")
#         print(f"Price: {self.price}")
#         print(f"Year: {self.year}")
#         print(f"Color: {self.color}")
#         print(f"Engine: {self.engine}")
#
#     def start_engine(self):
#         print(f" {self.model}'ning dvigateli hozir ishlayapti.")
#
# class BMW(Car):
#     def __init__(self, model, price, year, color, engine):
#         super().__init__(model, price, year, color, engine)
#
#     def display_info(self):
#         super().display_info()
#
#     def auto_park_assist(self):
#         print(f"{self.model} avtomatik mashinalar yordamchisi mavjud.")
#
# class Malibu(Car):
#     def __init__(self, model, price, year, color, engine):
#         super().__init__(model, price, year, color, engine)
#
#     def display_info(self):
#         super().display_info()
#
#     def hybrid_mode(self):
#         print(f"{self.model} gibrid haydash rejimiga ega.")
#
# class Lamborghini(Car):
#     def __init__(self, model, price, year, color, engine):
#         super().__init__(model, price, year, color, engine)
#
#     def display_info(self):
#         super().display_info()
#
#     def activate_launch_control(self):
#         print(f"{self.model}'ishga tushirishni boshqarish faollashtirilgan.")
#
# bmw = BMW("BMW X5", 60000, 2022, "Black", "V8")
# malibu = Malibu("Chevrolet Malibu", 35000, 2022, "Silver", "4-cylinder")
# lamborghini = Lamborghini("Lamborghini Aventador", 400000, 2022, "Red", "V12")
#
# cars = [bmw, malibu, lamborghini]
#
# for car in cars:
#     car.display_info()
#     car.start_engine()
#     print("\n")

#==============================================================================

# 2 - Masala

import math

class Figure:
    def __init__(self, name):
        self.name = name

    def display_info(self):
        print(f"Figure: {self.name}")

    def calculate_area(self):
        pass

class Triangle(Figure):
    def __init__(self, name, a, b, c):
        super().__init__(name)
        self.a = a
        self.b = b
        self.c = c

    def display_info(self):
        super().display_info()
        print(f"Sides: {self.a}, {self.b}, {self.c}")

    def calculate_area(self):
        s = (self.a + self.b + self.c) / 2
        area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        return area

class Circle(Figure):
    def __init__(self, name, r):
        super().__init__(name)
        self.r = r

    def display_info(self):
        super().display_info()
        print(f"Radius: {self.r}")

    def calculate_area(self):
        area = math.pi * (self.r ** 2)
        return area

class Square(Figure):
    def __init__(self, name, a, b):
        super().__init__(name)
        self.a = a
        self.b = b

    def display_info(self):
        super().display_info()
        print(f"Sides: {self.a}, {self.b}")

    def calculate_area(self):
        area = self.a * self.b
        return area

triangle = Triangle("Triangle", 3, 4, 5)
circle = Circle("Circle", 2)
square = Square("Square", 4, 4)

figures = [triangle, circle, square]
for figure in figures:
    figure.display_info()
    print(f"Area: {figure.calculate_area()}\n")

