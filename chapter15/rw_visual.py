# import matplotlib.pyplot as plt

# from random_walk import RandomWalk
# #keep making new walks, as long as the program is active
# while True:
#     #make a random walk
#     rw = RandomWalk()
#     rw.fill_walk()

#     #plot the points in the walk
#     plt.style.use('classic')
#     fig, ax = plt.subplots()
#     piont_numbers = range(rw.num_points)
#     # #pylint: disable = E1101
#     ax.scatter(rw.x_values, rw.y_values, c=piont_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)
#     # #pylint: disable = E1101

#     plt.show()

#     keep_running = input("Make another walk? (y/n): ")
#     if keep_running == 'n':
#         break


# import matplotlib.pyplot as plt

# from random_walk import RandomWalk

# #Make a random walk
# rw = RandomWalk()
# rw.fill_walk()

# #plot the points in the walk
# plt.style.use('classic')
# fig, ax = plt.subplots()
# ax.scatter(rw.x_values, rw.y_values, s=15)
# plt.show()

"""generating multiple random walks"""
import matplotlib.pyplot as plt

from random_walk import RandomWalk

#keep making new walks, as long as the program is active
# while True:
# #Make a random walk
#     rw = RandomWalk()
#     rw.fill_walk()

#     #plot the points in the walk
#     plt.style.use('classic')
#     fig, ax = plt.subplots()
#     ax.scatter(rw.x_values, rw.y_values, s=15)
#     plt.show()

#     keep_running = input("Make another walk? (y/n)")
#     if keep_running == 'n':
#         break

"""coloring the points"""
while True:
#Make a random walk
    rw = RandomWalk()
    rw.fill_walk()

#plot the points in the walk
    plt.style.use('classic')
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
#pylint: disable = #1101
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)
#pylint: disable = #1101
    plt.show()

    keep_running = input("Make another walk? (y/n)")
    if keep_running == 'n':
        break



