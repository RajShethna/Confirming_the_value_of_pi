#The project confirms the value of pi in mathematics by finding the perimeter of polygon of sides 1 to 100 inscribed within a circle of radius 1 to 5 units. Using graphical representation and mathematical analysis, value of pi can be confirmed.
# This project was executed by Raj Vijay Shethna on January 28, 2025.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

def Perimeter(r,n):
    P = 2*n*r*abs(math.sin(math.radians(180/n)))
    return P

Perimeter_list = []
n = list(range(3,103)) #100 samples
r = list(range(1,6))

for i in r:

    Perimeter_list_per_radius = []

    for j in n:
        P = Perimeter(i,j)
        Perimeter_list_per_radius.append(P)

    Perimeter_list.append(Perimeter_list_per_radius)

#Graphical Representation of Perimeter vs Number of Sides of Polygon for different radius
# for i in r:
#     plt.plot(Perimeter_list[i-1])
# plt.xlabel("Number of Sides of Polygon")
# plt.ylabel("Perimeter")
# plt.title("Perimeter vs Number of Sides with 1 <= r <= 5")
# plt.legend(loc='upper center')
# plt.grid(True)
# plt.show()

#Perimeter of the 100 sided polygon vs different radius
for i in r:
    globals()["P100_r" + str(i)] = Perimeter_list[i-1][99] #list starts with [0][0], therefore the -1 from the indices

#Analysis
print("Dividing the Perimeter of 100-sided Polygon within circle of radius 5 with 2*r5 is "+ str(P100_r5/(2*5)))
print("Dividing the Perimeter of 100-sided Polygon within circle of radius 4 with 2*r4 is "+ str(P100_r4/(2*4)))
print("Dividing the Perimeter of 100-sided Polygon within circle of radius 3 with 2*r3 is "+ str(P100_r3/(2*3)))
print("Dividing the Perimeter of 100-sided Polygon within circle of radius 2 with 2*r2 is "+ str(P100_r2/(2*2)))
print("Dividing the Perimeter of 100-sided Polygon within circle of radius 1 with 2*r1 is "+ str(P100_r1/(2*1)))

# The output printed from the above-written code is "3.141095972729376" for all the 5 lines of "print" codes. Hence value of pi is confirmed.
