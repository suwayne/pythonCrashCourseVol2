"""generating multiple random walks."""
"""also have solutions for ex15_4 and ex15_5"""
import matplotlib.pyplot as plt

from random_walk import RandomWalk

#keep making new walks, as long as the program is active.
while True:
    # Make a random walk.
    rw = RandomWalk(90_000)
    rw.fill_walk()
    # rw.get_step()

    # Plot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9), dpi=100)
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    # Emphasize the first and last points.
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break

