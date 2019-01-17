#Great Lake State Charts
#Sasha Falenchuk
#1/16/19
#5 graphs and charts analyzing Great Lakes states area, population, median income, median age, and economy
#This project was very fun, and I got to explore matplotlib quite a bit and do some cool and unique graphs. It took a quite a bit of effort to find some good data sets.
#Used matplotlib.org
#On my honor I have neither given nor received unauthorized aid


import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
 
objects = ("Minnesota", "Wisconsin", "Michigan", "Illinois", "Indiana", "Ohio", "Pennsylvania", "New York")
y_pos = np.arange(len(objects))
landarea = [79607,54154,56528,55518,35823,40858,44739,47126]
waterarea= [7328, 11342, 40185, 2398, 594, 3967, 1316, 7429]
 
p1 = plt.bar(y_pos, landarea, color=(0, .6, .2, 1))
p2 = plt.bar(y_pos, waterarea, color=(0, .4, 1, 1))
plt.xticks(y_pos, objects)
#plt.ylabel("Water Area")
plt.ylabel("Area")
plt.xlabel("Great Lake States")
plt.title("Great Lakes Land and Water Area")
plt.legend((p1[0], p2[0]), ("Land", "Water"))
 
plt.show()