"""this is how you plot a single point"""

import matplotlib.pyplot as plt
plt.style.use('seaborn')
fig, ax = plt.subplots()
# ax.scatter(2, 4, s=100)
#plotting a series of points
# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]

#calculating values automatically
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]
#changing the color of the line by passing c to the scatter method
# ax.scatter(x_values, y_values, s=5, c=(0, 0.8, 0))
#using a color map
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Greens, s=4)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

#set the range for each axis.
ax.axis([0, 1100, 0, 1100000])

# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)
# plt.show()

#saving your plot automatically
plt.savefig('squares_plot.png', bbox_inches='tight')

