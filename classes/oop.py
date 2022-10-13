import random


class Car:

    # Attributes
    def __init__(self):
        self.model = None
        self.colour = None
        self.speed = None

    def __int__(self, model, colour, speed):
        self.model = model
        self.colour = colour
        self.speed = speed

    # Model Method
    def set_model(self, model):
        self.model = model

    def get_model(self):
        return "Car model is : ", self.model

    # Colour Method
    def set_colour(self, colour):
        self.colour = colour

    def get_colour(self):
        return "Car colour is : ", self.colour

    # Speed Method
    def set_speed(self, speed):
        self.speed = speed

    def get_speed(self):
        return "Car speed is : ", self.speed

    # Behaviour
    def can_race(self):
        if self.speed >= 155:
            return "Car can race"
        else:
            return "Car can't race"


# Inheritance

class Toyota(Car):
    def sound(self, model):
        return 'the sound of is ', self.model, 'pimm'


class Jeep(Car):
    def sound(self, model):
        return 'the sound of is ', self.model, 'pum! pum! pum!'


# Objects
bmw = Jeep()
bmw.set_colour("white")
bmw.get_colour()
bmw.set_speed(147)

camry = Toyota()
camry.set_speed(158)
camry.get_speed()

Car.can_race(bmw)
Car.can_race(camry)
camry.model = "Camry"
camry.sound("")
bmw.model = "BMW"
bmw.sound("")


def roll():
    first = random.randint(1, 6)
    second = random.randint(1, 6)
    return first, second


class Dice:
    pass


# Factory in OOP
A = type("BaseClass", (object,), {})
B = type("B", (A,), {'val': 'Created Inherited Class 1'})
C = type("B", (A,), {'val': 20})


def class_creator(val):
    if val:
        return B()
    else:
        return C()

# To call the function
# print(class_creator(True).val)
# print(class_creator(False).val)
