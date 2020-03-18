""" Charles Jerome R. Sabio
    DATALOG Lab01
    Feb 5, 2020
    I have neither received nor provided any help on this (lab) activity, nor
    have I concealed any violation of the Honor Code.
"""

num = int(input("Type a number to see how many times you can divide it by 2 "   #asks for the input to be processed
                "before getting a value less than 2: "))

answer = num//2 #declares the operation to be used on the input
num = num%2 #adds modulo to the operation

print(answer) #prints the final output