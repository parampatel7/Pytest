import math

import pytest
import samplecode.shapes as shapes

#Shows how can we just need to assign circle parameters once via class 
class TestCircle:
    def setup_method(self, method):
            print(f"\nSetting up {method}\n")
            self.circle = shapes.Circle(10)

    def teardown_method(self, method):
        print(f"\nSetting up{method}\n")
        del self.circle 

    def test_area(self):
        x = math.pi * self.circle.radius ** 2
        print(x)
        assert self.circle.area() == x


    def test_perimeter(self):
         result = self.circle.perimeter()
         expected = 2 * math.pi * self.circle.radius
         assert result == expected

    def test_not_same_area_rectangle(self, my_rectangle):
         assert self.circle.area() != my_rectangle.area()