from abc import ABC , abstractmethod
class Area(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Area):
    def __init__(self,height,width):
        self.height = height
        self.width = width
    def area(self):
        print( self.height*self.width)
class Circle(Area):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        print( 3.14*(self.radius*self.radius))

area = [Rectangle(7,5),Circle(5)]
for i in area:
    i.area()
