import random
import matplotlib.pyplot as plt

results = []
for j in range(1000):
	total = 0
	for i in range(10):
		flip = random.randint(0,1)
		total += flip
	results.append(total)

display = [0 for i in range(11)]
for i in range(len(results)):
	display[results[i]] += 1

x_axis = [x for x in range (5,16)]
data2 = [y for y in range(5,16)]

#plt.plot(display)
#plt.plot(x_axis, display, 'b*', x_axis, data2, 'r^')
plt.bar(x_axis, display, color=(.5, 0., .5, 1.))
plt.ylabel("Number of Trials")
plt.xlabel("Number of Heads")
plt.show()
