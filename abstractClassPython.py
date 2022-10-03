class Shape:
    def getArea(self):
        pass

class Triangle(Shape):
    def __init__(self, base, height):
        self.base=base
        self.height=height
    def getArea(self):
        return 0.5*self.base*self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius=radius
    def getArea(self):
        return 3.14*self.radius*self.radius

AreaTriangle = Triangle(10,20)
print("Area Triangle = ", AreaTriangle.getArea())

AreaCirle = Circle(10)
print("Area Circle = ", AreaCirle.getArea())
