import math


class Shape:
    def area (self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    

class Rectangle(Shape):
    def __init__ (self, len, width):
        self.len = len
        self.width= width

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return False
        return self.width == other.width and self.len == other.len

    def area(self):
        return self.len * self.width
    def perimeter(self):
        return 2 * (self.len + self.width)
    

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)
# python3 -m pytest tests/test_rectangle.py  -v -s
# python3 -m pytest tests/test_shapes.py  -v -s