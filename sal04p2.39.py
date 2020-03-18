""" Charles Jerome R. Sabio
    DATALOG Lab01
    Feb 12, 2020
    I have neither received nor provided any help on this (lab) activity, nor
    have I concealed any violation of the Honor Code.
"""

from abc import ABCMeta, abstractmethod # defines the variables
def __init__(self):
    self.number_of_sides = len(lengths_of_sides)
    self.lengths_of_sides = [0] * self.number_of_sides
    self.assign_values_to_sides(lengths_of_sides)

    @abstractmethod
    def area (self): #Returns the area of the POLYGON.
        return area()

    @abstractmethod
    def perimeter(self):  # Return the perimeter of the POLYGON.
        return perimeter()

class Polygon(metaclass=ABCMeta): #Our own version of collections.Sequence abstract base class.

    @abstractmethod
    def __len__ (self): #Return the length of the sequence.

        @abstractmethod
        def __getitem__ (self, j): #Return the element at index j of the sequence.

            def __contains__ (self, val): #Return True if val found in the sequence; False otherwise.”””
                for j in range(len(self)):
                    if self[j] == val: # found match
                        return True
            return False

class Triangle(metaclass=ABCMeta):
    def __init__(self, lengths_of_sides):
        super().__init__(lengths_of_sides)

    def area(self):  # Returns the area of the Triangle.
        area_tri = 0.5 * base * height
        return area_tri

    def perimeter(self):  # Return the perimeter of the Triangle.
        peri_tri = a + b + c
        return peri_tri

        super().__init__(lengths_of_sides)
    assert 3, self.number_of_sides

class IscoscelesTriangle(metaclass=ABCMeta):
    def __init__(self, lengths_of_sides):
        super().__init__(lengths_of_sides)

    def area(self):  # Returns the area of the Triangle.
        area_iscotri = 0.5 * base * height
        return area_iscotri

    def perimeter(self):  # Return the perimeter of the Triangle.
        peri_iscotri = a + b + c
        return peri_iscotri

        super().__init__(lengths_of_sides)
    assert 3, self.number_of_sides






def index(self, val): #Return leftmost index at which val is found (or raise ValueError).”””
    for j in range(len(self)):
        if self[j] == val: # leftmost match
            return j
    raise ValueError( value not in sequence ) # never found a match

def count(self, val): #Return the number of elements equal to given value.
    k=0
    for j in range(len(self)):
            if self[j] == val: # found a match
                k += 1
    return k

Octagon = 2*(1+1.41)*(a*a)
Pentagon = (5.196 / 2 )*a  # a = number of sides
Hexagonarea = (sqrt(5 * (5 + 2 *(sqrt(5)))) * a * a) / 4
rectanglearea = lenght * width
triangle = 0.5 * base * height