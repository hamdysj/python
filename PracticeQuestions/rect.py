class Rectangle:

    def __init__(self, l, w):
        self.len = l
        self.wid = w

    def area(self):
        return "Area(Rectangle): ", self.len * self.wid


shape = Rectangle(8, 24)
print(shape.area())