""" Charles Jerome R. Sabio
    DATALOG Lab01
    Feb 5, 2020
    I have neither received nor provided any help on this (lab) activity, nor
    have I concealed any violation of the Honor Code.
"""

Price = float(input("Enter how much the product costs: "))    # asks for the 1st input
Payment = float(input("Enter the amount of payment: "))   # asks for the 2nd input
change = Payment - Price    # calculates the amount to be processed

thou = change//1000 # finds out how many 1000 can be given
change = change%1000 # returns the remainder of the bills to be changed
fivh = change//500 # finds out how many 500 can be given
change = change%500 # returns the remainder of the bills to be changed
twoh = change//200 # finds out how many 200 can be given
change = change%200 # returns the remainder of the bills to be changed
oneh = change//100 # finds out how many 100 can be given
change = change%100 # returns the remainder of the bills to be changed
fif = change//50 # finds out how many 50 can be given
change = change%50 # returns the remainder of the bills to be changed
twen = change//20 # finds out how many 20 can be given
change = change%20 # returns the remainder of the bills to be changed
ten = change//10 # finds out how many 10 can be given
change = change%10 # returns the remainder of the bills to be changed
fiv = change//5 # finds out how many 5 can be given
change = change%5 # returns the remainder of the bills to be changed
one = change//1 # finds out how many 1 can be given
change = change%1 # returns the remainder of the bills to be changed
cen = change//.25 # finds out how many .25 can be given
#change = change%.25 # returns the remainder of the bills to be changed

print("1000 peso bills: ", (thou))  # prints output
print("500 peso bills: ", (fivh))   # prints output
print("200 peso bills: ", (twoh))   # prints output
print("100 peso bills: ", (oneh))   # prints output
print("50 peso bills: ", (fif))     # prints output
print("20 peso bills: ", (twen))    # prints output
print("10 peso coins: ", (ten))     # prints output
print("5 peso coins: ", (fiv))      # prints output
print("1 peso coins: ", (one))      # prints output
print("25 cents: ", (cen))          # prints output