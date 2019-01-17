import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
 
objects = ("1950", "1960", "1970", "1980", "1990", "2000", "2010")
y_pos = np.arange(len(objects))
minnesota = [2.997,  3.425,  3.806,  4.076,  4.390,  4.934, 5.311]
wisconsin = [3.438,  3.962,  4.418,  4.706,  4.905,  5.374, 5.691]
michigan = [6.407,  7.834,  8.882,  9.262,  9.311,  9.952,  9.878]
illinois = [8.738,  10.090,  11.110,  11.430,  11.450, 12.430, 12.840]
indiana = [3.967, 4.674, 5.195,  5.490, 5.558, 6.092, 6.491]
ohio = [7.980, 9.734, 10.660, 10.800, 10.860, 11.360, 11.540]
pennsylvania = [10.510, 11.330, 11.800, 11.860, 11.900, 12.280, 12.710]
newyork = [14.860, 16.840, 18.240, 17.560, 18.020, 19.000, 19.390,]

p1 = plt.plot(y_pos, minnesota, marker='o', color=(0.6, .2, .9, 1))
p2 = plt.plot(y_pos, wisconsin, marker='o', color=(0.7, 0, 0, 1))
p3 = plt.plot(y_pos, michigan, marker='o', color=(1, .6, .2, 1))
p4 = plt.plot(y_pos, illinois, marker='o', color=(1, 0,0, 1))
p5 = plt.plot(y_pos, indiana, marker='o', color=(0, 1, 0, 1))
p6 = plt.plot(y_pos, ohio, marker='o', color=(0, 0, 1, 1))
p7 = plt.plot(y_pos, pennsylvania, marker='o', color=(0, .4, 1, 1))
p8 = plt.plot(y_pos, newyork, marker='o', color=(0.3, .5, .5, 1))
plt.xticks(y_pos, objects)
plt.ylabel("Populations in Millions")
plt.xlabel("Years 1980 - 2015")
plt.title("Great Lakes States Population 1980 - 2015")
plt.legend((p1[0], p2[0], p3[0], p4[0], p5[0], p6[0], p7[0], p8[0]),("Minnesota", "Wisconsin", "Michigan", "Illinois", "Indiana", "Ohio", "Pennsylvania", "New York"))
 
plt.show()