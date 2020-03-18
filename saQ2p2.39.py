""" Charles Jerome R. Sabio
    DATALOG Lab01
    Feb 19, 2020
    I have neither received nor provided any help on this (lab) activity, nor
    have I concealed any violation of the Honor Code.
"""


class Polygon():

    def __init__(self, lengths_of_sides):
        self.number_of_sides = len(lengths_of_sides)
        self.lengths_of_sides = [0] * [self.number_of_sides]

    def print_num_sides(self):
        '''a quick, informational print statement'''
        print('There are ' + str(self.number_of_sides) + 'sides.')


class Pentagon(Polygon):

    def __init__(self, lengths_of_sides):
        Polygon.__init__(self, 5, lengths_of_sides)

    def area(self):
        x, y = self.lenghts_of_sides[0], self.lenghts_of_sides[1]
        return x * y

    def perimeter(self):
        '''Return the perimeter of the polygon.'''
        # calculate the perimeter
        x, y = self.lenghts_of_sides
        return (x + y) * 2


class Hexagon(Polygon):

    def __init__(self, lengths_of_sides):
        Polygon.__init__(self, 6, lengths_of_sides)

    def area(self):
        x, y = self.lenghts_of_sides[0], self.lenghts_of_sides[1]
        return x * y

    def perimeter(self):
        '''Return the perimeter of the polygon.'''
        # calculate the perimeter
        x, y = self.lenghts_of_sides
        return (x + y) * 2