#land area compared to water area
import matplotlib.pyplot as plt

labels =  "Great Lake States Average Water Area - 9,319.875 square miles", "Great Lake States Average Land Area - 51,794.125 square miles"
sizes = [ 9319.875, 51794.125]
colors = ['lakeblue, earthgreen']
explode = (0.1, .1)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels,
        shadow=True, startangle=90)
ax1.axis('equal')
plt.title("Great Lake States Average Area - 61,114 square miles")
plt.show()