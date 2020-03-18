""" Charles Jerome R. Sabio
    DATALOG Lab05
    Feb 19, 2020
    I have neither received nor provided any help on this (lab) activity, nor
    have I concealed any violation of the Honor Code.
"""

import matplotlib.pyplot as plt #imports the matplotlib.pyplot library in this file
import numpy as np #sets numpy as np
n = np.linspace(10, 10**9, 100) #the range of n in the function
plt.xlabel('log x') #prints the label of the x-axis
plt.ylabel('log y') #prints the label of the y-axis
plt.title("Plot of R-3.1\n" "CJRSabio >> DATALOG LAB05 << Feb. 19, 2020  \n N3710 @ 1.60GHz, Windows 10 \n") #Title Block
plt.xscale('log') #prints the scale of the x-axis
plt.yscale('log') #prints the scale of the y-axis

y1 = 8*n #set as multiplication function
y2 = 4*n*np.log(n) #set as logarithmic function
y3 = 2*n**2 #set as exponential function
y4 = n**3 #set as exponent function

plt.plot(n, y1, label = '8n') #graphs the multiplication function
plt.plot(n, y2, label = '4nlog(n)') #graphs the logarithmic function
plt.plot(n, y3, label = '2n\u00b2') #graphs the exponential function
plt.plot(n, y4, label = 'n\u00b3') #graphs the exponential function
plt.legend() #prints the label in the graph
plt.show() #prints the graph