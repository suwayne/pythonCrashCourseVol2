# import numpy as np
# import matplotlib.pyplot as plt
# ....................................
# from matplotlib import pyplot as plt

# x_values = range(1, 5001)
# y_values = [x**3 for x in x_values]

# plt.style.use('seaborn')
# fig, ax = plt.subplots()

# #pylint: disable = E1101
# ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)
# #pylint: enable = E1101

# # set chart title and label axis.
# ax.set_title("Cube Numbers", fontsize=24)
# ax.set_xlabel("Value", fontsize=14)
# ax.set_ylabel("Cube of Value", fontsize=14)

# # set size of tick labels.
# ax.tick_params(axis='both', which='major', labelsize=14)

# # set the range of each axis.
# ax.axis([0, 1100, 0, 1100000])

# plt.show()
# ...............................................

from matplotlib import pyplot as plt

# define data.
x_values = [1, 2, 3, 4, 5]
cubes = [1, 8, 27, 64, 125]

# make plot.
plt.style.use('seaborn')
fix, ax = plt.subplots()
ax.scatter(x_values, cubes, edgecolor='none', s=40)

# set chart title and label axes.
ax.set_title("cubes", fontsize=24)
ax.set_xlabel("value", fontsize=14)
ax.set_ylabel("cube of value", fontsize=14)

# set size of tick labels.
ax.tick_params(axis='both', labelsize=14)

# set size of tick labels.
ax.tick_params(axis='both', labelsize=14)

# show plot.
plt.show()
