import random

class Car():

    #Attributes
    def __int__(self,model,colour,speed):
        self.model = model
        self.colour = colour
        self.speed = speed

    #Model Method
    def setmodel(self, model):
        self.model = model
    def getmodel(self):
        print("Car model is : ", self.model)

    #Colour Method
    def setcolour(self, colour):
            self.colour = colour
    def getcolour(self):
            print("Car colour is : ", self.colour)

    #Speed Method
    def setspeed(self, speed):
            self.speed = speed
    def getspeed(self):
            print("Car speed is : ", self.speed)

    #Behaviour
    def canRace(self):
        if(self.speed) >= 155:
            print("Car can race")
        else:
            print("Car can't race")

### Inheritance

class Toyota(Car):
    def sound(self, model):
        print('the sound of is ', self.model, 'pimmmmmmmmmm')

class Jeep(Car):
    def sound(self, model):
        print('the sound of is ', self.model, 'pum! pum! pum!')


#Objects
bmw = Jeep()
bmw.setcolour("white")
bmw.getcolour()
bmw.setspeed(147)

camry = Toyota()
camry.setspeed(158)
camry.getspeed()

Car.canRace(bmw)
Car.canRace(camry)
camry.model = "Camry"
camry.sound("")
bmw.model = "BMW"
bmw.sound("")


class Dice:

    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return first, second

d1 = Dice()
print(d1.roll())





