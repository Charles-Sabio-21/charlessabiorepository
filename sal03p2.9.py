""" Charles Jerome R. Sabio
    DATALOG Lab01
    Feb 12, 2020
    I have neither received nor provided any help on this (lab) activity, nor
    have I concealed any violation of the Honor Code.
"""

class Vector:
    """Represent a vector in a multidimensional space."""

    def __init__(self, d):
        if isinstance(d, int):
            self._coords = [0] * d
        else:
            try:  # we test if param is iterable
                self._coords = [val for val in d]
            except TypeError:
                raise TypeError('invalid parameter type')

    def __len__(self):
        """Return the dimension of the vector."""
        return len(self._coords)

    def __getitem__(self, j):
        """Return jth coordinate of vector."""
        return self._coords[j]

    def __setitem__(self, j, val):
        """Set jth coordinate of vector to given value."""
        self._coords[j] = val

    def __add__(self, other):
        """Return sum of two vectors."""
        if len(self) != len(other):  # relies on __len__ method
            raise ValueError('dimensions must agree')
        result = Vector(len(self))  # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __sub__(self, other):
        if len(self) != len(other):  # relies on __len__ method
            raise ValueError('dimensions must agree')
        result = Vector(len(self))  # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    def __str__(self):
        """Produce string representation of vector."""
        return '<' + str(self._coords)[1:-1] + '>'  # adapt list representation


if __name__ == '__main__':
    # the following demonstrates usage of a few methods
    v = Vector(8)  # construct line of 8 digits
    v[1] = 10  # <0, 10, 0, 0, 0, 0, 0, 0> (based on use of __setitem__)
    v[-1] = 18  # <0, 10, 0, 0, 0, 0, 0, 18> (also via __setitem__)
    print(v[2])  # print 0 (via __getitem__)
    u = v + v  # <0, 20, 0, 0, 0, 0, 0, 36> (via __add__)
    print(u)  # print <0, 20, 0, 0, 0, 0, 0, 36>
    w = v - u
    print(w)
    total = 0
    for entry in v:  # implicit iteration using __len__ and __getitem__
        total += entry