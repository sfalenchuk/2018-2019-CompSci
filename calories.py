import random
import matplotlib.pyplot as plt

results = []
for i in range(10):
	party = random.randint(1,10)
	meal = random.randint(1,8)
	calories = random.randint(40, 520)
	total = party*meal*calories
results.append(total)

display = [0 for i in range(11)]
for i in range(len(results)):
	display[results[i]]

x_axis = [x for x in range (1,100s)]
data2 = [y for y in range(1,520)]

#plt.plot(display)
#plt.plot(x_axis, display, 'b*', x_axis, data2, 'r^')
#plt.bar(x_axis, display, color=(.5, 0., .5, 1.))
#plt.ylabel("")
#plt.xlabel("")
plt.show()
