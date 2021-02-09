# import matplotlib.pyplot as plt

# input_values = [1, 2, 3, 4, 5]
# squares = [1, 4, 9, 16, 25]

# plt.style.use('seaborn-paper')
# fig, ax = plt.subplots()
# ax.plot(input_values, squares, linewidth =1)

# #set chart title and label axes.
# ax.set_title("Square Numbers", fontsize=7)
# ax.set_xlabel("Value", fontsize=14)
# ax.set_ylabel("Square of Value", fontsize=7)

# #size of tick labels.
# ax.tick_params(axis='both', labelsize=14)

# plt.show()

#scatter squares
# import matplotlib.pyplot as plt

# plt.style.use('seaborn')
# fig, ax = plt.subplots()
# ax.scatter(2, 4, s=200)

# #set chart title and label axes.
# ax.set_title("Square Numbers", fontsize=14)
# ax.set_xlabel("Value", fontsize=14)
# ax.set_ylabel("Square of Value", fontsize=14)

# #set size of tick labels.
# ax.tick_params(axis='both', which='major', labelsize=14)

# plt.show()

# import matplotlib.pyplot as plt

# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]

# plt.style.use('seaborn')    
# fig, ax = plt.subplots()
# ax.scatter(x_values, y_values, s=20)

# #set chart title and label axes.
# ax.set_title("Square of Numbers", fontsize=12)
# ax.set_xlabel("Value", fontsize=12)
# ax.set_ylabel("Square", fontsize=12)

# #set size of tick labels.
# ax.tick_params(axis='both', which='major', labelsize=12)

# plt.show()


# import matplotlib.pyplot as plt

# x_values = range(1, 1001)
# y_values = [x**2 for x in x_values]

# plt.style.use('seaborn')
# fig, ax = plt.subplots()
# #pylint: disable = #1101
# ax.scatter(x_values, y_values,c=y_values, cmap=plt.cm.Blues, s=3)
# #pylint: disable = #1101


# #set chart title and label axes.
# ax.set_title("Square of Numbers", fontsize=12)
# ax.set_xlabel("Value", fontsize=12)
# ax.set_ylabel("Square", fontsize=12)

# #set size of tick labels.
# ax.tick_params(axis='both', which='major', labelsize=12)

# #set range for each axes
# ax.axis([0, 1100, 0, 1100000])

# plt.show()

#saving your plots automatically
# plt.savefig('squares_plot.png', bbox_inches='tight')

# import matplotlib.pyplot as plt

# x_values = range(1, 1001)
# y_values = [x**3 for x in x_values]

# plt.style.use('seaborn')
# fig, ax = plt.subplots()

# #pylint: disable = #1101
# ax.scatter(x_values, y_values,c=y_values, cmap=plt.cm.Blues, s=3)
# #pylint: disable = #1101


# #set chart title and label axes.
# ax.set_title("Square of Numbers", fontsize=12)
# ax.set_xlabel("Value", fontsize=12)
# ax.set_ylabel("Square", fontsize=12)

# #set size of tick labels.
# ax.tick_params(axis='both', which='major', labelsize=12)

# plt.show()

# #saving your plots automatically
# plt.savefig('squares_plot.png', bbox_inches='tight')



import matplotlib.pyplot as plt

from random_walk import RandomWalk
"""coloring the points"""

while True:
#Make a random walk
    rw = RandomWalk(50_000)
    rw.fill_walk()

#plot the points in the walk
    plt.style.use('classic')
#adding figsize to fill up the screen with the plot.
    fig, ax = plt.subplots(figsize=(15, 9))
    point_numbers = range(rw.num_points)
#pylint: disable = #1101
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)
#pylint: disable = #1101

#emphasize the first and last points.
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

#remove the axes 
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)


    plt.show()

    keep_running = input("Make another walk? (y/n)")
    if keep_running == 'n':
        break
