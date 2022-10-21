class Circle:

    def __init__(self, r):
        self.rad = r

    def area(self):
        pie = 2.14
        return "Area of a circle with radius %d: " % self.rad, pie * self.rad * self.rad

    def perimeter(self):
        pie = 2.14
        return "Perimeter of a circle with radius %d: " % self.rad, 2*pie*self.rad


shape = Circle(8) 
print(shape.area(), shape.perimeter())
