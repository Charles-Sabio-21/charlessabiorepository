""" Charles Jerome R. Sabio
    DATALOG Lab01
    Feb 10, 2020
    I have neither received nor provided any help on this (lab) activity, nor
    have I concealed any violation of the Honor Code.
"""

def diff_num(m): # Declaring of the statement of the whole code.
                # def is used to mark the start of a function
    return sorted(m) == list(range(min(m), max(m) + 1))
    # This syntax is the sorted() function of Python.
    # We compare the sorted list with list of range of minimum and
    # maximum integer of the list and return it.

one = [2, 3, 1, 4, 5] # set the 1st list to be processed
two = [2, 1, 4, 2, 1] # set the 2nd list to be processed
print("Set 1: " ,(one), "has different numbers: ") # prints the 1st list
print(diff_num(one)) # prints the result of the applied function
print("Set 2: " ,(two), "has different numbers: ") # prints the 2nd list
print(diff_num(two)) # prints the result of the applied function