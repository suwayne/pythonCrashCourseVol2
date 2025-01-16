import matplotlib.pyplot as plt

from random_walk import RandomWalk
"""coloring the points"""

while True:
#Make a random walk
    rw = RandomWalk(5000)
    rw.fill_walk()

#plot the points in the walk
    plt.style.use('classic')
#adding figsize to fill up the screen with the plot.
    fig, ax = plt.subplots(figsize=(15, 9))
    point_numbers = range(rw.num_points)

#replacing .scatter with .plot
    ax.plot(rw.x_values, rw.y_values, linewidth=1)
  
#pylint: disable = #1101
    # ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)
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
