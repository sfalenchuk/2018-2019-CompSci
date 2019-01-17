import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.broken_barh([(2014, 1), (2012, 1), (2009, 1), (2006, 1)], (30, 10), facecolors='blue')
ax.broken_barh([(2005, 1), (2009, 3), (2013, 1)], (10, 10),
               facecolors=("red"))
ax.set_ylim(0, 50)
ax.set_xlim(2005, 2015)
ax.set_xlabel("Years (2005 - 2015)")
ax.set_yticks([15, 35])
ax.set_yticklabels(["Michigan", "Illinois"])
ax.grid(True)
ax.annotate("periods of economic growth", (2011, 20),
            xytext=(.9, .9), textcoords='axes fraction',
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=16,
            horizontalalignment='right', verticalalignment='top')

plt.show()